const FIELDS = ['myName', 'context', 'firstPrompt', 'replyPrompt'];
const $ = (id) => document.getElementById(id);

// ---------------------------------------------------------------- Onglets

function showTab(name) {
  for (const b of document.querySelectorAll('[data-tab]')) b.setAttribute('aria-selected', String(b.dataset.tab === name));
  for (const p of document.querySelectorAll('[data-panel]')) p.hidden = p.dataset.panel !== name;
  try { localStorage.setItem('tab', name); } catch {}
}
for (const b of document.querySelectorAll('[data-tab]')) b.addEventListener('click', () => showTab(b.dataset.tab));
try { if (localStorage.getItem('tab')) showTab(localStorage.getItem('tab')); } catch {}

// ---------------------------------------------------------------- Prompts

chrome.storage.local.get(COPIE_DM_DEFAULTS, (s) => {
  for (const f of FIELDS) $(f).value = s[f];
});

$('save').addEventListener('click', () => {
  const values = {};
  for (const f of FIELDS) values[f] = $(f).value;
  values.myName = values.myName.trim() || 'Moi';
  chrome.storage.local.set(values, () => {
    $('saved').textContent = '✓ Enregistré';
    setTimeout(() => ($('saved').textContent = ''), 2000);
  });
});

for (const b of document.querySelectorAll('[data-reset]')) {
  b.addEventListener('click', () => {
    for (const f of b.dataset.reset.split(',')) $(f).value = COPIE_DM_DEFAULTS[f];
    $('saved').textContent = 'Pense à enregistrer.';
  });
}

// ---------------------------------------------------------------- Suivi

let suivi = [];
const pct = (n, d) => (d ? Math.round((n / d) * 100) + ' %' : '—');

function renderStats() {
  const sent = suivi.length;
  const replied = suivi.filter((e) => e.replied).length;
  const page = suivi.filter((e) => e.page).length;
  $('stats').innerHTML = `
    <div class="stat"><b>Premiers messages</b><span class="big">${sent}</span><small>préparés</small></div>
    <div class="stat"><b>Réponses</b><span class="big">${pct(replied, sent)}</span><small>${replied} sur ${sent}</small></div>
    <div class="stat"><b>Pages créées</b><span class="big">${pct(page, sent)}</span><small>${page} sur ${sent}</small></div>`;
}

function renderRows() {
  $('empty').hidden = suivi.length > 0;
  $('rows').innerHTML = '';
  suivi.forEach((e, i) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${new Date(e.date).toLocaleDateString('fr-FR')}</td>
      <td><a target="_blank" rel="noopener"></a></td>
      <td class="c"><input type="checkbox" data-k="replied"></td>
      <td class="c"><input type="checkbox" data-k="page"></td>
      <td class="c"><button class="del" title="Retirer (message pas envoyé)">✕</button></td>`;
    const a = tr.querySelector('a');
    a.href = 'https://www.instagram.com/' + encodeURIComponent(e.user) + '/';
    a.textContent = '@' + e.user;
    for (const cb of tr.querySelectorAll('input')) {
      cb.checked = !!e[cb.dataset.k];
      cb.addEventListener('change', () => {
        suivi[i][cb.dataset.k] = cb.checked;
        chrome.storage.local.set({ suivi });
      });
    }
    tr.querySelector('.del').addEventListener('click', () => {
      if (!confirm(`Retirer @${e.user} du suivi ?`)) return;
      suivi.splice(i, 1);
      chrome.storage.local.set({ suivi });
    });
    $('rows').appendChild(tr);
  });
}

function load() {
  chrome.storage.local.get({ suivi: [] }, (s) => {
    suivi = s.suivi;
    renderStats();
    renderRows();
  });
}
load();
// Se met à jour tout seul quand un premier message est préparé dans l'onglet Instagram.
chrome.storage.onChanged.addListener((changes) => { if (changes.suivi) load(); });

$('export').addEventListener('click', () => {
  const lines = [['date', 'equipage', 'a_repondu', 'page_creee']]
    .concat(suivi.map((e) => [e.date, '@' + e.user, e.replied ? 'oui' : 'non', e.page ? 'oui' : 'non']));
  const csv = lines.map((l) => l.join(';')).join('\n');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob(['﻿' + csv], { type: 'text/csv' }));
  a.download = `suivi-premiers-messages-${new Date().toISOString().slice(0, 10)}.csv`;
  a.click();
});
