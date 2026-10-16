// Captures de la page j4l-club (https://trophytracker.fr/road-trip/j4l-club), le road trip qui sert d'exemple.
//   node captures-j4l.mjs france   → la vraie page (trace en France), sans le numéro d'équipage ni le texte du carnet
//   node captures-j4l.mjs desert   → la même page, mise en scène dans les dunes : on remplace la trace, la position
//                                    et le carnet par une journée de piste (demande de Julien, 16/10/2026).
//                                    Météo réelle à cette position, nom de lieu masqué.
// Sortie : captures-j4l/<F|D>_*.png (3× la largeur d'un téléphone).
import { chromium } from 'playwright-core';
import fs from 'fs';
import { fileURLToPath } from 'url';
const MODE0 = process.argv[2] || 'france';
// « sansreseau » : comme « desert », mais le dernier point date de 2 h (la page affiche alors le bandeau « pas de réseau »)
const OFF = MODE0 === 'sansreseau';
const MODE = OFF ? 'desert' : MODE0;
const OUT = fileURLToPath(new URL('./captures-j4l/', import.meta.url));
fs.mkdirSync(OUT, { recursive: true });
const P = OFF ? 'N_' : MODE === 'desert' ? 'D_' : 'F_';
const LAG = OFF ? 2.1 * 3600e3 : 60e3;
const exe = process.env.HOME + '/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome';
const b = await chromium.launch({ executablePath: exe, args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const ctx = await b.newContext({ viewport: { width: 430, height: 932 }, deviceScaleFactor: 3, locale: 'fr-FR', timezoneId: 'Africa/Casablanca' });
const p = await ctx.newPage();

// ───────── journée de piste autour des dunes (points en pixels d'une mosaïque z12, convertis en lat/lon) ─────────
const Z = 12, N = 2 ** Z, X0 = 2000, Y0 = 1673;
const ll = ([px, py]) => { const x = X0 + px / 256, y = Y0 + py / 256; return [Math.atan(Math.sinh(Math.PI * (1 - 2 * y / N))) * 180 / Math.PI, x / N * 360 - 180]; };
const WAY = [[690, 60], [672, 130], [640, 190], [585, 222], [548, 262], [538, 318], [548, 380], [560, 440], [578, 500], [600, 556], [606, 620], [604, 690], [618, 752], [655, 790], [712, 772], [760, 720], [790, 650], [800, 585], [796, 520]];
function track() {
  const now = Date.now(), pts = [];
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const dense = [];
  for (let i = 0; i < WAY.length - 1; i++) for (let k = 0; k < 40; k++) {
    const t = k / 40, a = WAY[i], c = WAY[i + 1];
    dense.push([a[0] + (c[0] - a[0]) * t + (rnd() - .5) * 2.2, a[1] + (c[1] - a[1]) * t + (rnd() - .5) * 2.2]);
  }
  dense.push(WAY[WAY.length - 1]);
  const t0 = now - 5.2 * 3600e3 - LAG, dt = (now - LAG - t0) / dense.length;
  dense.forEach((q, i) => { const [la, lo] = ll(q); pts.push([+la.toFixed(6), +lo.toFixed(6), Math.round((t0 + i * dt) / 1000), Math.round(28 + rnd() * 30), Math.round(712 + 40 * Math.sin(i / 50) + rnd() * 12)]); });
  return pts;
}
const TRACK = MODE === 'desert' ? track() : null;
const LAST = TRACK && TRACK[TRACK.length - 1];
const DAY = (d) => new Date(Date.now() - d * 864e5).toISOString().slice(0, 10);

await p.route('**/*', async (route) => {
  const u = route.request().url();
  const json = (obj) => route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(obj) });
  const orig = async () => { const r = await route.fetch(); return r.json(); };
  if (u.includes('/rest/v1/crews?')) {
    const j = await orig();
    j[0].car_number = null; j[0].story = '';
    if (MODE === 'desert') Object.assign(j[0], { last_lat: LAST[0], last_lon: LAST[1], city: null, last_speed_kmh: 38, last_fix_at: new Date(Date.now() - LAG).toISOString(), tracking_enabled: true, tracking_stopped_at: null, total_distance_m: 3021400, starts_on: DAY(8), start_lat: TRACK[0][0], start_lon: TRACK[0][1] });
    return json(j);
  }
  if (MODE !== 'desert') return route.continue();
  if (u.includes('/rpc/get_track')) return json(TRACK);
  if (u.includes('/rpc/get_telemetry')) return json({ lat: LAST[0], lon: LAST[1], today: { distance_km: 71.6, max_altitude: 784, moving_minutes: 262 }, course: 12, battery: 64, accuracy: 6, altitude: 731, speed_kmh: 38, recorded_at: new Date(Date.now() - LAG + 40e3).toISOString() });
  if (u.includes('/rpc/get_crew_stats')) return json({ live: !OFF, last_fix_at: new Date(Date.now() - LAG).toISOString(), points_count: 8412, avg_speed_kmh: 41, followers_count: 0, current_speed_kmh: 38, total_distance_km: 3021.4 });
  if (u.includes('photon.komoot.io')) return json({ type: 'FeatureCollection', features: [] });
  if (u.includes('/rest/v1/sponsors?')) { const j = await orig(); j.forEach(s => { s.lat = null; s.lon = null; }); return json(j); }
  if (u.includes('/rest/v1/photos?')) { const j = await orig(); j.forEach(s => { s.lat = null; s.lon = null; }); return json(j); }
  if (u.includes('/rest/v1/trip_stages?')) {
    const st = (kind, name, note, px, d) => { const [lat, lon] = ll(px); return { id: crypto.randomUUID(), crew_id: 'x', kind, name, note, place: null, lat, lon, arrived_at: null, left_at: null, source: 'manual', created_by: null, created_at: new Date(Date.now() - d * 36e5).toISOString(), updated_at: new Date().toISOString() }; };
    return json([st('night', 'Bivouac au pied des dunes', null, [540, 300], 20), st('highlight', 'Le bout de la piste', 'Du sable à perte de vue, pause photo obligatoire.', [640, 785], 3)]);
  }
  if (u.includes('/rest/v1/journal_entries?')) return json([{ id: 'j1', crew_id: 'x', day: DAY(1), title: 'Le feu de camp', body: "Une journée entière de piste, le sable partout, même dans les sandwichs. Le soir, feu de camp avec les autres équipages et des étoiles comme on n'en voit jamais chez nous.", ai_generated: true, published: true, created_by: null, created_at: new Date().toISOString(), updated_at: new Date().toISOString() }]);
  return route.continue();
});

await p.goto('https://trophytracker.fr/road-trip/j4l-club', { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
await p.waitForTimeout(8000);
for (let y = 0; y < 9000; y += 600) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(250); }
await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(2500);

const box = (sel) => p.evaluate((sel) => { const e = document.querySelector(sel); if (!e) return null; const r = e.getBoundingClientRect(); return { x: r.left, y: r.top + scrollY, width: r.width, height: r.height }; }, sel);
const boxText = (text, tag) => p.evaluate(([text, tag]) => {
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n;
  while ((n = w.nextNode())) if (n.textContent.trim().toLowerCase().startsWith(text.toLowerCase())) { const e = n.parentElement.closest(tag); if (e) { const r = e.getBoundingClientRect(); return { x: r.left, y: r.top + scrollY, width: r.width, height: r.height }; } }
  return null; }, [text, tag]);
async function shot(name, r, pad = 0) {
  if (!r) { console.log('MANQUE', name); return; }
  await p.screenshot({ path: OUT + P + name + '.png', fullPage: true, clip: { x: Math.max(0, r.x - pad), y: Math.max(0, r.y - pad), width: r.width + 2 * pad, height: r.height + 2 * pad } });
  console.log('ok', P + name);
}
async function screen(name, y) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(1200); await p.screenshot({ path: OUT + P + name + '.png' }); console.log('ok', P + name); }

const MAP = '[aria-label^="Carte du road trip"]';
const sec = (pref) => `section[aria-label^="${pref}"]`;
await shot('couverture', await box('section'));
await screen('ecran_haut', 0);
const m = await box(MAP);
await screen('ecran_carte', Math.max(0, m.y - 70));
await p.waitForTimeout(6000);
await shot('carte', m);
if (MODE === 'france') { for (let i = 0; i < 4; i++) { await p.click('button[aria-label="Zoom out"]').catch(() => {}); await p.waitForTimeout(800); } await p.waitForTimeout(4000); await shot('carte_large', await box(MAP)); }
await p.click('text=Relief 3D').catch(e => console.log('relief', e.message)); await p.waitForTimeout(10000);
await screen('ecran_relief', Math.max(0, m.y - 70)); await p.waitForTimeout(6000);
await screen('ecran_relief', Math.max(0, m.y - 70));
await shot('relief3d', await box(MAP));
await p.click('text=Satellite').catch(() => {}); await p.waitForTimeout(3000);
const dash = await p.evaluate(() => { const m = document.querySelector('[aria-label^="Carte du road trip"]').getBoundingClientRect(); const w = [...document.querySelectorAll('section')].find(s => (s.getAttribute('aria-label') || '').startsWith('Météo')); const t = w.getBoundingClientRect(); return { x: m.left, y: m.bottom + scrollY + 8, width: m.width, height: t.top - m.bottom - 12 }; });
await shot('tableau_de_bord', dash);
await shot('meteo', await box(sec('Météo')));
await shot('profil_altitude', await boxText('Profil d’altitude', 'div[class*="rounded"]'));
await shot('bandeau_reseau', await boxText('Pas de nouvelle position', 'p, div'), 6);
if (OFF) await shot('carte_pas_de_reseau', await boxText('Pas de réseau, c’est normal', 'div[class*="rounded"]'));
await shot('replay_bloc', await boxText('revivre en 3D', 'section'));
await shot('carnet', await boxText('Carnet de route', 'section'));
if (MODE === 'desert') { await p.click('role=tab[name="Journal"]').catch(async () => { await p.click('text=Journal').catch(e => console.log('journal', e.message)); }); await p.waitForTimeout(1500); await shot('carnet_journal', await boxText('Carnet de route', 'section')); }
await shot('photos', await boxText('Photos', 'section'));
await shot('sponsors', await boxText('ils soutiennent ce voyage', 'section'));
await shot('mur', await boxText('mur d’encouragements', 'section'));
const etat = await p.evaluate(() => { const t = document.body.innerText; return t.slice(0, 900); });
console.log(etat);
await b.close();
