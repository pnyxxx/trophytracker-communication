import { chromium } from 'playwright-core';
const exe = process.env.HOME + '/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome';
const b = await chromium.launch({ executablePath: exe, args: ['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
const p = await b.newPage({ viewport: { width: 430, height: 932 }, deviceScaleFactor: 3 });
await p.goto('https://trophytracker.fr/road-trip/exemple', { waitUntil: 'networkidle', timeout: 60000 }).catch(()=>{});
await p.waitForTimeout(7000);
// faire charger les photos (lazy)
for (let y = 0; y < 6000; y += 600) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(250); }
await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(1500);
const rect = (fn) => p.evaluate(fn);
async function shotEl(sel, name, pad = 0) {
  const r = await p.evaluate(([sel]) => { const e = typeof sel === 'string' ? document.querySelector(sel) : null; if (!e) return null; const b = e.getBoundingClientRect(); return { x: b.left, y: b.top + scrollY, width: b.width, height: b.height }; }, [sel]);
  if (!r) { console.log('MANQUE', name, sel); return; }
  await p.screenshot({ path: new URL('./captures/', import.meta.url).pathname + `${name}.png`, fullPage: true, clip: { x: Math.max(0, r.x - pad), y: Math.max(0, r.y - pad), width: r.width + 2 * pad, height: r.height + 2 * pad } });
  console.log('ok', name, Math.round(r.y), Math.round(r.height));
}
async function shotClosest(text, name, tagSel = 'section', pad = 0) {
  const r = await p.evaluate(([text, tagSel]) => {
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n; while ((n = w.nextNode())) if (n.textContent.trim().toLowerCase().startsWith(text.toLowerCase())) { const e = n.parentElement.closest(tagSel); if (e) { const b = e.getBoundingClientRect(); return { x: b.left, y: b.top + scrollY, width: b.width, height: b.height }; } }
    return null; }, [text, tagSel]);
  if (!r) { console.log('MANQUE', name, text); return; }
  await p.screenshot({ path: new URL('./captures/', import.meta.url).pathname + `${name}.png`, fullPage: true, clip: { x: Math.max(0, r.x - pad), y: Math.max(0, r.y - pad), width: r.width + 2 * pad, height: r.height + 2 * pad } });
  console.log('ok', name, Math.round(r.y), Math.round(r.height));
}
await shotEl('section', 'C1_couverture');
// carte : dézoomer pour voir toute la trace
const map = '[aria-label^="Carte du road trip"]';
await shotEl(map, 'C2a_carte_depart');
for (let i = 0; i < 3; i++) { await p.click('button[aria-label="Zoom out"]').catch(()=>{}); await p.waitForTimeout(700); }
await p.waitForTimeout(5000);
await shotEl(map, 'C2_carte_trace');
await p.click('text=Relief 3D').catch(e=>console.log('relief', e.message));
await p.waitForTimeout(9000);
await shotEl(map, 'C3_relief3d');
await p.click('text=Satellite').catch(()=>{});
// tableau de bord = entre la carte et la météo
const dash = await p.evaluate(() => { const m = document.querySelector('[aria-label^="Carte du road trip"]').getBoundingClientRect(); const w = [...document.querySelectorAll('section')].find(s => (s.getAttribute('aria-label')||'').startsWith('Météo')); const t = w.getBoundingClientRect(); return { y0: m.bottom + scrollY, y1: t.top + scrollY, x: m.left, w: m.width }; });
await p.screenshot({ path: new URL('./captures/C4_tableau_de_bord.png', import.meta.url).pathname, fullPage: true, clip: { x: dash.x, y: dash.y0 + 8, width: dash.w, height: dash.y1 - dash.y0 - 12 } });
await shotEl('section[aria-label^="Météo"]', 'C5_meteo');
await shotClosest('Profil d’altitude', 'C6_profil_altitude', 'div.rounded-\\[22px\\], div[class*="rounded"]');
await shotClosest('revivre en 3D', 'C11b_replay_bloc');
await shotClosest('Carnet de route', 'C7a_carnet_etapes');
await p.click('role=tab[name="Journal"]').catch(async () => { await p.click('text=Journal').catch(e=>console.log('journal', e.message)); });
await p.waitForTimeout(1500);
await shotClosest('Carnet de route', 'C7_carnet_journal');
console.log('JOURNAL:', (await p.evaluate(() => { const s=[...document.querySelectorAll('section')].find(s=>s.textContent.includes('Carnet de route')); return s ? s.innerText.slice(0,1500) : ''; })));
await p.click('text=Histoire').catch(()=>{}); await p.waitForTimeout(1200);
await shotClosest('Carnet de route', 'C7b_carnet_histoire');
await shotClosest('Photos', 'C21_photos', 'section');
await shotClosest('ils soutiennent ce voyage', 'C18_sponsors');
await shotClosest('mur d’encouragements', 'C12_mur');
console.log('MUR:', (await p.evaluate(() => { const s=[...document.querySelectorAll('section')].find(s=>s.textContent.includes('encouragements')); return s ? s.innerText.slice(0,800) : ''; })));
await b.close();
