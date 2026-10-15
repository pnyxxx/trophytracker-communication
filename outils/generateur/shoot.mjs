import { chromium } from 'playwright-core';
import fs from 'fs'; import path from 'path';
const jobs = JSON.parse(fs.readFileSync(new URL("./jobs.json", import.meta.url)));
const exe = process.env.HOME + '/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome';
const b = await chromium.launch({ executablePath: exe, args: ['--allow-file-access-from-files'] });
const N = 4; let i = 0, done = 0;
async function worker() {
  const ctx = await b.newContext({ deviceScaleFactor: 2, viewport: { width: 1080, height: 1920 } });
  const p = await ctx.newPage();
  while (i < jobs.length) {
    const j = jobs[i++];
    await p.setViewportSize({ width: j.w, height: j.h });
    await p.goto('file://' + j.html, { waitUntil: 'load' });
    await p.waitForFunction(() => document.body.dataset.ready === '1', null, { timeout: 30000 }).catch(() => console.log('timeout', j.html));
    await p.waitForTimeout(150);
    fs.mkdirSync(path.dirname(j.png), { recursive: true });
    await p.screenshot({ path: j.png, clip: { x: 0, y: 0, width: j.w, height: j.h } });
    if (++done % 20 === 0) console.log(done, '/', jobs.length);
  }
  await ctx.close();
}
await Promise.all(Array.from({ length: N }, worker));
await b.close();
console.log('fini', done);
