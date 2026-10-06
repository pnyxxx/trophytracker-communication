// TrophyTracker DM — s'exécute sur instagram.com.
// Sur une conversation (/direct/t/…) : remonte l'historique, récupère chaque message dans l'ordre, et copie
// la conversation seule ou un prompt pour y répondre.
// Sur le profil ou une publication d'un équipage : prépare un prompt pour écrire le premier message.
// Rien n'est envoyé nulle part : l'extension lit seulement ce qui est affiché à l'écran.
(() => {
  'use strict';
  if (window.__copieDmInsta) return;
  window.__copieDmInsta = true;

  const DEFAULTS = COPIE_DM_DEFAULTS;

  // Les boutons du panneau. Pour en ajouter un : une ligne ici + son prompt dans defaults.js (et options.html).
  const ACTIONS = [
    { id: 'copy', label: '📋 Copier les messages', withPrompt: false },
    { id: 'reply', label: '✨ Générer une réponse', withPrompt: true, promptKey: 'replyPrompt' }
  ];

  // Petits textes d'interface Instagram à ne pas prendre pour des messages.
  const IGNORE_RE = /^(vu|seen|lu|read|envoyé|sent|distribué|delivered|vu par .+|seen by .+|vu il y a .+|seen .+ ago|voir le profil|view profile|actif|active|active now|en ligne|online|actif il y a .+|active .+ ago|en train d'écrire.*|typing.*|écrit.*\.\.\.)$/i;

  // Libellé ARIA de la liste des messages (anglais / français).
  const CONVO_LABEL =
    '[aria-label^="Messages in conversation"], [aria-label^="Messages dans la conversation"], ' +
    '[aria-label^="Conversation with"], [aria-label^="Conversation avec"]';

  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  // Premiers segments d'adresse qui ne sont pas des noms de compte.
  const RESERVED = new Set(['explore', 'direct', 'accounts', 'reels', 'stories', 'p', 'reel', 'tv', 'about', 'legal',
    'developer', 'web', 'emails', 'challenge', 'notifications', 'your_activity', 'settings', 'privacy', 'session',
    'api', 'graphql', 'oauth', 'directory', 'lite', 'topics', 'locations', 'tags', 'invites', 'meta-verified']);

  // 'thread' (conversation), 'profile' (profil d'un compte), 'post' (publication), ou null.
  function pageType() {
    const parts = location.pathname.split('/').filter(Boolean);
    if (parts[0] === 'direct' && parts[1] === 't') return 'thread';
    if (['p', 'reel', 'tv'].includes(parts[0]) && parts[1]) return 'post';
    if (parts.length >= 3 && ['p', 'reel'].includes(parts[1])) return 'post';
    if (parts[0] && !RESERVED.has(parts[0]) && /^[A-Za-z0-9._]+$/.test(parts[0]) &&
      (parts.length === 1 || ['reels', 'tagged', 'followers', 'following'].includes(parts[1]))) return 'profile';
    return null;
  }

  function getSettings() {
    return new Promise((resolve) => {
      try {
        chrome.storage.local.get(DEFAULTS, (s) => resolve({ ...DEFAULTS, ...(s || {}) }));
      } catch {
        // Extension rechargée sans recharger la page : on garde les valeurs par défaut.
        resolve({ ...DEFAULTS });
      }
    });
  }

  function getLocal(key, fallback) {
    return new Promise((resolve) => {
      try {
        chrome.storage.local.get({ [key]: fallback }, (s) => resolve(s[key]));
      } catch {
        resolve(fallback);
      }
    });
  }

  function setLocal(values) {
    return new Promise((resolve) => {
      try {
        chrome.storage.local.set(values, resolve);
      } catch {
        resolve();
      }
    });
  }

  // ---------------------------------------------------------------- Trouver la zone des messages

  function isScrollableStyle(el) {
    const oy = getComputedStyle(el).overflowY;
    return oy === 'auto' || oy === 'scroll';
  }

  function scrollCandidates() {
    const vh = window.innerHeight;
    const out = [];
    for (const el of document.querySelectorAll('div, section, main')) {
      if (el.closest('#copie-dm-insta-host')) continue;
      if (!isScrollableStyle(el)) continue;
      const r = el.getBoundingClientRect();
      if (r.width < 250 || r.height < vh * 0.3) continue;
      out.push({ el, r, overflow: el.scrollHeight - el.clientHeight > 10 });
    }
    return out;
  }

  // Le plus intérieur d'abord, et de préférence celui qui défile vraiment.
  function pick(list) {
    list.sort((a, b) => (b.overflow - a.overflow) || (a.r.width * a.r.height - b.r.width * b.r.height));
    return list[0] ? list[0].el : null;
  }

  function findContainer() {
    const cands = scrollCandidates();
    if (!cands.length) return null;
    const labeled = document.querySelector(CONVO_LABEL);
    if (labeled) {
      const rel = cands.filter((c) => c.el.contains(labeled) || labeled.contains(c.el));
      if (rel.length) return pick(rel);
    }
    // Sinon : la zone qui défile la plus à droite (la liste des conversations est à gauche).
    const maxLeft = Math.max(...cands.map((c) => c.r.left));
    return pick(cands.filter((c) => c.r.left >= maxLeft - 40));
  }

  function guessContactName(container) {
    const labeled = document.querySelector(CONVO_LABEL);
    if (labeled) {
      const m = (labeled.getAttribute('aria-label') || '').match(/(?:with|avec)\s+(.+)$/i);
      if (m) return m[1].trim();
    }
    // Le nom en gras dans l'en-tête, juste au-dessus de la zone des messages.
    const c = container.getBoundingClientRect();
    for (const el of document.querySelectorAll('h1, h2, span, a')) {
      if (el.closest('#copie-dm-insta-host') || container.contains(el)) continue;
      if (el.children.length > 2) continue;
      const text = (el.textContent || '').trim();
      if (!text || text.length > 60) continue;
      const r = el.getBoundingClientRect();
      if (r.height < 8 || r.bottom > c.top + 4 || r.top < c.top - 140) continue;
      if (r.left < c.left || r.right > c.right) continue;
      if (parseInt(getComputedStyle(el).fontWeight, 10) >= 600) return text;
    }
    return '';
  }

  // ---------------------------------------------------------------- Lire les messages affichés

  // Texte d'un élément, en gardant les émojis affichés en image et les retours à la ligne.
  function textOf(el) {
    let out = '';
    const walk = (n) => {
      if (n.nodeType === Node.TEXT_NODE) out += n.nodeValue;
      else if (n.nodeType === Node.ELEMENT_NODE) {
        if (n.tagName === 'BR') out += '\n';
        else if (n.tagName === 'IMG') out += n.getAttribute('alt') || '';
        else for (const ch of n.childNodes) walk(ch);
      }
    };
    walk(el);
    return out.replace(/ /g, ' ').replace(/[ \t]+\n/g, '\n').trim();
  }

  function sideOf(r, c) {
    const leftGap = r.left - c.left;
    const rightGap = c.right - r.right;
    if (Math.abs(leftGap - rightGap) < c.width * 0.08) return 'center';
    return rightGap < leftGap ? 'me' : 'them';
  }

  // Tous les messages actuellement présents dans la page, dans l'ordre visuel (haut → bas).
  function snapshot(container) {
    const c = container.getBoundingClientRect();
    const units = [];

    for (const el of container.querySelectorAll('[dir="auto"]')) {
      const outer = el.parentElement && el.parentElement.closest('[dir="auto"]');
      if (outer && outer !== container && container.contains(outer)) continue;
      if (el.closest('[contenteditable="true"], textarea, input')) continue;
      const text = textOf(el);
      if (!text || IGNORE_RE.test(text)) continue;
      const range = document.createRange();
      range.selectNodeContents(el);
      const r = range.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) continue;
      units.push({ node: el, text, rect: r, side: sideOf(r, c) });
    }

    for (const m of container.querySelectorAll('img, video')) {
      if (m.closest('[dir="auto"]')) continue;
      const r = m.getBoundingClientRect();
      if (r.width < 80 || r.height < 80) continue; // photos de profil, émojis…
      const a = m.closest('a[href]');
      const href = a ? a.getAttribute('href') : '';
      let text;
      if (href && /\/(p|reel|reels|tv|stories)\//.test(href)) {
        text = '[publication partagée : ' + new URL(href, location.origin).href.split('?')[0] + ']';
      } else {
        text = m.tagName === 'VIDEO' ? '[vidéo]' : '[photo]';
      }
      units.push({ node: m, text, rect: r, side: sideOf(r, c) });
    }

    units.sort((a, b) => (a.rect.top - b.rect.top) || (a.rect.left - b.rect.left));
    return units;
  }

  // Assemble les relevés successifs pris pendant le défilement, même si Instagram retire de la page
  // les messages qui sortent de l'écran : chaque élément affiché garde un identifiant, et les nouveaux
  // messages sont insérés à côté de ceux déjà connus.
  function createCollector() {
    const ids = new WeakMap();
    const items = new Map();
    const order = [];
    let nextId = 1;

    const keyOf = (x) => x.side + '|' + x.text;
    const remember = (u, id) => {
      ids.set(u.node, { id, text: u.text });
      return id;
    };

    // Instagram recrée parfois les éléments d'un message déjà lu : on le reconnaît alors à son contenu,
    // soit parce qu'il suit le dernier message reconnu, soit (en début de relevé) parce qu'au moins
    // 3 messages d'affilée correspondent à une suite déjà connue.
    function alignAt(units, k) {
      const need = Math.min(3, units.length - k);
      let best = -1;
      let bestLen = 0;
      for (let j = 0; j < order.length; j++) {
        let len = 0;
        while (k + len < units.length && j + len < order.length && keyOf(items.get(order[j + len])) === keyOf(units[k + len])) len++;
        if (len >= need && len >= bestLen) {
          best = j;
          bestLen = len;
        }
      }
      return best;
    }

    function idFor(units, k, cursor) {
      const u = units[k];
      const rec = ids.get(u.node);
      if (rec && rec.text === u.text) return rec.id;
      if (cursor !== null) {
        const next = order[cursor + 1];
        if (next !== undefined && keyOf(items.get(next)) === keyOf(u)) return remember(u, next);
      } else if (order.length) {
        const j = alignAt(units, k);
        if (j !== -1) return remember(u, order[j]);
      }
      return remember(u, nextId++);
    }

    function merge(units) {
      let pending = [];
      let cursor = null;
      for (let k = 0; k < units.length; k++) {
        const u = units[k];
        const id = idFor(units, k, cursor);
        if (items.has(id)) {
          let idx = order.indexOf(id);
          if (pending.length) {
            order.splice(idx, 0, ...pending);
            idx += pending.length;
            pending = [];
          }
          cursor = idx;
        } else {
          items.set(id, { side: u.side, text: u.text });
          if (cursor === null) pending.push(id);
          else order.splice(++cursor, 0, id);
        }
      }
      // Aucun message connu dans ce relevé : on remonte l'historique, donc c'est plus ancien.
      if (pending.length) order.unshift(...pending);
    }

    return { merge, entries: () => order.map((id) => items.get(id)), size: () => order.length };
  }

  async function loadFullHistory(container, collector, onProgress, shouldStop) {
    collector.merge(snapshot(container));
    let stuck = 0;
    for (let i = 0; i < 5000 && !shouldStop(); i++) {
      const before = container.scrollTop;
      const height = container.scrollHeight;
      container.scrollTop = before - container.clientHeight * 0.8;
      await sleep(250);
      collector.merge(snapshot(container));
      onProgress(collector.size());
      if (Math.abs(container.scrollTop - before) >= 2) {
        stuck = 0;
        continue;
      }
      // En haut : on attend qu'Instagram charge les messages plus anciens.
      const loading = () => container.querySelector('[role="progressbar"], [aria-label*="Chargement"], [aria-label*="Loading"]');
      const t0 = Date.now();
      let grew = false;
      while (!shouldStop() && Date.now() - t0 < (loading() ? 8000 : 3000)) {
        await sleep(250);
        if (container.scrollHeight !== height || Math.abs(container.scrollTop - before) >= 2) {
          grew = true;
          break;
        }
      }
      collector.merge(snapshot(container));
      onProgress(collector.size());
      if (grew) {
        stuck = 0;
        continue;
      }
      // Petit aller-retour pour relancer le chargement, puis on considère qu'on est au début.
      if (++stuck >= 2) break;
      container.scrollTop = before + 200;
      await sleep(300);
      container.scrollTop = before - 200;
      await sleep(300);
    }
    collector.merge(snapshot(container));
    container.scrollTop = container.scrollHeight; // retour aux derniers messages
  }

  // ---------------------------------------------------------------- Mise en texte

  const today = () =>
    new Date().toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });

  function formatConversation(entries, names) {
    const lines = [];
    let count = 0;
    for (const e of entries) {
      if (e.side === 'center') {
        lines.push('--- ' + e.text.replace(/\n+/g, ' ') + ' ---');
        continue;
      }
      count++;
      const who = e.side === 'me' ? names.me : names.them;
      lines.push(who + ' : ' + e.text.replace(/\n/g, '\n    '));
    }
    const head = `=== Conversation Instagram entre ${names.me} et ${names.them} — ${count} messages (copiée le ${today()}) ===`;
    return { text: head + '\n' + lines.join('\n') + '\n=== Fin de la conversation ===', count };
  }

  // Texte final d'une action : la conversation seule, ou contexte du projet + conversation + consigne.
  function buildOutput(action, entries, names, settings) {
    const conv = formatConversation(entries, names);
    if (!action.withPrompt) return conv;
    const fill = (s) =>
      (s || '').trim().replaceAll('{interlocuteur}', names.them).replaceAll('{moi}', names.me).replaceAll('{date}', today());
    const parts = [fill(settings.context), `Nous sommes le ${today()}.`, conv.text, fill(settings[action.promptKey])];
    return { text: parts.filter(Boolean).join('\n\n'), count: conv.count };
  }

  // ---------------------------------------------------------------- Premier message : lire l'équipage

  const UI_WORDS = new Set(['suivre', 'suivi(e)', 'suivi', 'abonné(e)', 'message', 'contacter', 'follow', 'following',
    'options', 'plus', 'more', 'suivre en retour', 'follow back', 'envoyer un message', 'voir la traduction']);
  const clip = (s, n) => (s.length > n ? s.slice(0, n) + '…' : s);
  const cleanText = (s) =>
    s.split('\n').map((l) => l.trim()).filter((l) => l && !UI_WORDS.has(l.toLowerCase())).join('\n');

  // La publication ouverte : en page entière, ou en fenêtre par-dessus un profil.
  const postScope = () =>
    document.querySelector('[role="dialog"] article') || document.querySelector('main article') ||
    document.querySelector('[role="dialog"]') || document.querySelector('main') || document.body;

  function readCrew() {
    const type = pageType();
    const parts = location.pathname.split('/').filter(Boolean);
    const info = { username: '', profile: '', posts: [], caption: '' };
    if (type === 'profile') {
      info.username = parts[0];
      const header = document.querySelector('main header') || document.querySelector('header');
      if (header) info.profile = clip(cleanText(header.innerText), 1500);
      info.posts = [...document.querySelectorAll('main a[href*="/p/"] img[alt], main a[href*="/reel/"] img[alt]')]
        .map((i) => i.getAttribute('alt').trim()).filter(Boolean).slice(0, 6).map((a) => clip(a, 300));
    }
    if (type === 'post') {
      const scope = postScope();
      if (['p', 'reel'].includes(parts[1])) info.username = parts[0];
      if (!info.username) {
        for (const a of scope.querySelectorAll('a[href]')) {
          const m = a.getAttribute('href').match(/^\/([A-Za-z0-9._]+)\/$/);
          if (m && !RESERVED.has(m[1]) && a.textContent.trim()) {
            info.username = m[1];
            break;
          }
        }
      }
      const h1 = scope.querySelector('h1');
      if (h1) info.caption = clip(textOf(h1), 1500);
    }
    return info;
  }

  function buildFirstMessage(info, username, note, settings) {
    const crew = [`Compte : @${username}`];
    if (info.profile) crew.push('Profil (en-tête du compte) :\n' + info.profile);
    if (info.posts.length) crew.push('Dernières publications (descriptions générées par Instagram) :\n' + info.posts.map((p) => '- ' + p).join('\n'));
    if (info.caption) crew.push('Publication que je viens de voir (légende) :\n' + info.caption);
    if (note) crew.push('Ce que j\'ai remarqué moi-même : ' + note);
    const fill = (s) =>
      (s || '').trim().replaceAll('{compte}', '@' + username)
        .replaceAll('{moi}', settings.myName).replaceAll('{date}', today());
    return [
      fill(settings.context),
      `Nous sommes le ${today()}.`,
      '=== Équipage à contacter (infos lues sur Instagram) ===\n' + crew.join('\n\n') + '\n=== Fin des infos ===',
      fill(settings.firstPrompt)
    ].filter(Boolean).join('\n\n');
  }

  // ---------------------------------------------------------------- Diagnostic (si la copie rate)

  function diagnostic() {
    const lines = [];
    lines.push('Diagnostic TrophyTracker DM v' + (chrome.runtime?.getManifest?.().version || '?'));
    lines.push(`Page : ${pageType()} — fenêtre ${innerWidth}x${innerHeight}`);
    let chosen;
    if (pageType() === 'thread') {
      const cands = scrollCandidates();
      chosen = findContainer();
      lines.push(`Libellé ARIA trouvé : ${!!document.querySelector(CONVO_LABEL)}`);
      lines.push('Zones qui défilent :');
      for (const c of cands) {
        lines.push(`  ${c.el === chosen ? '=>' : '  '} x=${Math.round(c.r.left)} y=${Math.round(c.r.top)} ${Math.round(c.r.width)}x${Math.round(c.r.height)} défile=${c.overflow} aria=${c.el.getAttribute('aria-label') || ''}`);
      }
    } else {
      const info = readCrew();
      lines.push(`Lu : compte=${info.username} | profil=${info.profile.length} car. | publications=${info.posts.length} | légende=${info.caption.length} car.`);
      chosen = pageType() === 'post' ? postScope() : document.querySelector('main header') || document.querySelector('main');
    }
    if (!chosen) return lines.join('\n');
    const base = chosen.getBoundingClientRect();
    lines.push('Arbre de la zone choisie (textes tronqués) :');
    let n = 0;
    const dump = (el, depth) => {
      if (n++ > 1500) return;
      const r = el.getBoundingClientRect();
      const attrs = [];
      for (const a of ['role', 'aria-label', 'dir', 'href', 'data-testid']) {
        const v = el.getAttribute(a);
        if (v) attrs.push(`${a}="${v.slice(0, 40)}"`);
      }
      const fd = getComputedStyle(el).flexDirection;
      if (fd === 'column-reverse') attrs.push('column-reverse');
      const own = [...el.childNodes].filter((c) => c.nodeType === 3).map((c) => c.nodeValue.trim()).join(' ');
      const txt = own ? ` "${own.slice(0, 15)}${own.length > 15 ? '…' : ''}"` : '';
      lines.push(`${'  '.repeat(depth)}${el.tagName.toLowerCase()} ${attrs.join(' ')} [${Math.round(r.left - base.left)},${Math.round(r.top - base.top)} ${Math.round(r.width)}x${Math.round(r.height)}]${txt}`);
      for (const ch of el.children) dump(ch, depth + 1);
    };
    dump(chosen, 0);
    return lines.join('\n');
  }

  // ---------------------------------------------------------------- Interface

  const host = document.createElement('div');
  host.id = 'copie-dm-insta-host';
  const root = host.attachShadow({ mode: 'open' });
  root.innerHTML = `
    <style>
      :host { all: initial; }
      * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
      .launcher { position: fixed; right: 20px; bottom: 96px; z-index: 2147483646; border: 0; border-radius: 999px;
        padding: 10px 16px; font-size: 14px; font-weight: 600; color: #fff; cursor: pointer;
        background: linear-gradient(135deg, #f58529, #dd2a7b 50%, #8134af); box-shadow: 0 4px 14px rgba(0,0,0,.25); }
      .launcher:hover { filter: brightness(1.08); }
      .panel { position: fixed; right: 20px; bottom: 96px; z-index: 2147483647; width: 380px; max-width: calc(100vw - 32px);
        background: #fff; color: #111; border-radius: 14px; box-shadow: 0 10px 40px rgba(0,0,0,.3); padding: 16px; font-size: 13px; }
      .panel[hidden], .launcher[hidden], [hidden] { display: none !important; }
      .row { display: flex; gap: 8px; align-items: center; margin-top: 10px; }
      h2 { margin: 0; font-size: 15px; flex: 1; }
      label { color: #555; white-space: nowrap; }
      input[type=text], select { flex: 1; min-width: 0; padding: 6px 8px; border: 1px solid #ccc; border-radius: 8px; font-size: 13px; }
      [data-zone="first"] label { width: 78px; }
      button { border: 0; border-radius: 8px; padding: 8px 12px; font-size: 13px; font-weight: 600; cursor: pointer; }
      .primary { background: #0095f6; color: #fff; flex: 1; }
      .actions { flex-wrap: wrap; }
      .actions .primary:nth-child(1) { background: #efefef; color: #111; }
      button:disabled { opacity: .5; cursor: default; }
      .check { display: flex; gap: 6px; align-items: center; cursor: pointer; }
      .secondary { background: #efefef; color: #111; }
      .close { background: none; font-size: 18px; padding: 0 4px; color: #777; }
      .status { margin-top: 10px; color: #333; min-height: 18px; }
      .status.ok { color: #0a7d32; font-weight: 600; }
      .status.err { color: #c62828; }
      textarea { width: 100%; height: 200px; margin-top: 8px; padding: 8px; border: 1px solid #ddd; border-radius: 8px;
        font: 12px/1.4 ui-monospace, Menlo, Consolas, monospace; resize: vertical; }
      .link { background: none; padding: 0; color: #888; font-weight: 400; font-size: 11px; text-decoration: underline; }
      @media (prefers-color-scheme: dark) {
        .panel { background: #262626; color: #f5f5f5; }
        label, .status { color: #ccc; }
        input[type=text], select, textarea { background: #1a1a1a; color: #f5f5f5; border-color: #444; }
        .secondary, .actions .primary:nth-child(1) { background: #3a3a3a; color: #f5f5f5; }
        .status.ok { color: #4cd07d; }
      }
    </style>
    <button class="launcher" hidden></button>
    <div class="panel" hidden>
      <div class="row" style="margin-top:0"><h2></h2><button class="close" title="Fermer">✕</button></div>
      <div data-zone="thread">
        <div class="row"><label for="them">Interlocuteur :</label><input id="them" type="text" placeholder="Nom de la personne"></div>
        <div class="row"><label class="check"><input id="full" type="checkbox" checked> Remonter tout l'historique</label></div>
        <div class="row actions"></div>
        <div class="row" hidden data-zone="stop"><button class="secondary" data-act="stop" style="flex:1">Arrêter et utiliser ce qui est chargé</button></div>
      </div>
      <div data-zone="first">
        <div class="row"><label for="crew">Équipage :</label><input id="crew" type="text" placeholder="@compte"></div>
        <div class="row"><label for="note">Remarqué :</label><input id="note" type="text" placeholder="un détail vu chez eux (facultatif)"></div>
        <div class="row"><button class="primary" data-act="first">✉️ Préparer le premier message</button></div>
      </div>
      <div class="status"></div>
      <div data-zone="result" hidden>
        <textarea spellcheck="false"></textarea>
        <div class="row"><button class="secondary" data-act="copy" style="flex:1">Copier à nouveau</button></div>
      </div>
      <div class="row" style="justify-content:flex-end"><button class="link" data-act="diag">Copier un diagnostic (si ça rate)</button></div>
    </div>`;

  const $ = (s) => root.querySelector(s);
  const launcher = $('.launcher');
  const panel = $('.panel');
  const themInput = $('#them');
  const fullInput = $('#full');
  const crewInput = $('#crew');
  const noteInput = $('#note');
  const status = $('.status');
  const textarea = $('textarea');
  for (const a of ACTIONS) {
    const b = document.createElement('button');
    b.className = 'primary';
    b.dataset.act = a.id;
    b.textContent = a.label;
    $('.actions').appendChild(b);
  }

  let running = false;
  let stopRequested = false;
  let lastAction = null;
  // Messages déjà lus pour la conversation ouverte : un 2e clic ne remonte pas tout l'historique,
  // il ajoute seulement les nouveaux messages.
  let session = null;

  const setStatus = (msg, cls = '') => {
    status.textContent = msg;
    status.className = 'status ' + cls;
  };

  async function copyText(text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      textarea.value = text;
      textarea.focus();
      textarea.select();
      try {
        return document.execCommand('copy');
      } catch {
        return false;
      }
    }
  }

  async function render() {
    if (!session || !lastAction) return;
    const settings = await getSettings();
    const names = { me: settings.myName.trim() || 'Moi', them: themInput.value.trim() || 'Interlocuteur' };
    const { text, count } = buildOutput(lastAction, session.collector.entries(), names, settings);
    textarea.value = text;
    $('[data-zone="result"]').hidden = false;
    if (!count) {
      setStatus("Aucun message trouvé. Clique sur « Copier un diagnostic » et envoie-le à Claude pour corriger l'extension.", 'err');
      return;
    }
    const ok = await copyText(text);
    const what = lastAction.withPrompt ? `Prompt copié (${count} messages)` : `${count} messages copiés`;
    setStatus(ok ? `✓ ${what} — colle dans Claude (Ctrl+V)` : 'Clique sur « Copier à nouveau » pour copier.', ok ? 'ok' : '');
  }

  const setBusy = (busy, showStop) => {
    running = busy;
    $('[data-zone="stop"]').hidden = !showStop;
    for (const b of root.querySelectorAll('.actions button')) b.disabled = busy;
  };

  async function run(action) {
    if (running) return;
    const container = findContainer();
    if (!container) {
      setStatus('Je ne trouve pas la zone des messages. Ouvre une conversation, puis réessaie.', 'err');
      return;
    }
    if (!session || session.path !== location.pathname) {
      session = { path: location.pathname, collector: createCollector(), full: false };
    }
    if (!themInput.value.trim()) themInput.value = guessContactName(container);
    lastAction = action;
    stopRequested = false;
    const needFull = fullInput.checked && !session.full;
    setBusy(true, needFull);
    try {
      if (needFull) {
        setStatus("Remontée de l'historique… (ne touche pas à la conversation)");
        await loadFullHistory(container, session.collector, (n) => setStatus(`Remontée de l'historique… ${n} éléments lus`), () => stopRequested);
        session.full = !stopRequested;
      } else {
        session.collector.merge(snapshot(container));
      }
      await render();
    } catch (e) {
      setStatus('Erreur : ' + e.message, 'err');
    } finally {
      setBusy(false, false);
    }
  }

  // Premier message : prompt pour Claude + enregistrement dans le suivi.
  async function runFirst() {
    const info = readCrew();
    const username = crewInput.value.trim().replace(/^@/, '') || info.username;
    if (!username) {
      setStatus("Je ne trouve pas le nom du compte. Écris-le dans « Équipage », puis réessaie.", 'err');
      return;
    }
    const settings = await getSettings();
    const suivi = await getLocal('suivi', []);
    if (!suivi.some((e) => e.user.toLowerCase() === username.toLowerCase())) {
      suivi.unshift({ user: username, date: new Date().toISOString().slice(0, 10), replied: false, page: false });
      await setLocal({ suivi });
    }

    const text = buildFirstMessage(info, username, noteInput.value.trim(), settings);
    textarea.value = text;
    $('[data-zone="result"]').hidden = false;
    const ok = await copyText(text);
    const thin = !info.profile && !info.caption && !noteInput.value.trim() ? ' Peu d\'infos lues : ajoute un détail dans « Remarqué ».' : '';
    setStatus(ok ? `✓ Prompt copié, noté dans ton suivi. Colle dans Claude.${thin}`
      : 'Clique sur « Copier à nouveau » pour copier.', ok ? 'ok' : '');
  }

  // Le panneau s'adapte à la page : conversation, ou profil / publication d'un équipage.
  function showPanelFor(type) {
    const isThread = type === 'thread';
    $('h2').textContent = isThread ? 'Conversation' : 'Premier message';
    $('[data-zone="thread"]').hidden = !isThread;
    $('[data-zone="first"]').hidden = isThread;
  }

  launcher.addEventListener('click', () => {
    const type = pageType();
    launcher.hidden = true;
    panel.hidden = false;
    showPanelFor(type);
    if (type !== 'thread') {
      crewInput.value = readCrew().username ? '@' + readCrew().username : '';
      noteInput.value = '';
      $('[data-zone="result"]').hidden = true;
      setStatus('');
      return;
    }
    if (!session || session.path !== location.pathname) {
      themInput.value = '';
      $('[data-zone="result"]').hidden = true;
      setStatus('');
    }
    const c = findContainer();
    if (c && !themInput.value.trim()) themInput.value = guessContactName(c);
  });
  $('.close').addEventListener('click', () => {
    stopRequested = true;
    panel.hidden = true;
    launcher.hidden = !pageType();
  });
  themInput.addEventListener('change', render);
  root.addEventListener('click', async (e) => {
    const act = e.target.closest('[data-act]')?.dataset.act;
    const action = ACTIONS.find((a) => a.id === act);
    if (action) run(action);
    else if (act === 'first') runFirst();
    else if (act === 'stop') stopRequested = true;
    else if (act === 'copy') {
      const ok = await copyText(textarea.value);
      setStatus(ok ? '✓ Copié' : 'Copie impossible : sélectionne le texte et fais Ctrl+C.', ok ? 'ok' : 'err');
    } else if (act === 'diag') {
      const ok = await copyText(diagnostic());
      setStatus(ok ? '✓ Diagnostic copié — colle-le à Claude.' : 'Copie du diagnostic impossible.', ok ? 'ok' : 'err');
    }
  });

  // Instagram change de page sans recharger : on vérifie l'adresse régulièrement.
  let lastPath = null;
  setInterval(() => {
    if (!host.isConnected) document.documentElement.appendChild(host);
    if (location.pathname === lastPath) return;
    lastPath = location.pathname;
    // Autre page : on referme le panneau et on adapte le bouton.
    stopRequested = true;
    panel.hidden = true;
    const type = pageType();
    launcher.hidden = !type;
    launcher.textContent = type === 'thread' ? '💬 TrophyTracker DM' : '✉️ Premier message';
  }, 800);
  document.documentElement.appendChild(host);
})();
