const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const files = process.argv.slice(2);
(async () => {
  const b = await chromium.launch(); const bad = [];
  for (const vp of [{ width: 1440, height: 900 }, { width: 390, height: 844 }]) {
    const ctx = await b.newContext({ viewport: vp }); const page = await ctx.newPage();
    await page.route(/googleapis|gstatic|maps\.google/, r => r.abort());
    await page.route('https://images.unsplash.com/**', r => { const f = '/root/ph/' + new URL(r.request().url()).pathname.slice(1) + '.jpg'; return fs.existsSync(f) ? r.fulfill({ contentType: 'image/jpeg', body: fs.readFileSync(f) }) : r.fulfill({ status: 404, body: '' }); });
    let errs = []; page.on('pageerror', e => errs.push(String(e)));
    for (const f of files) {
      errs = [];
      await page.goto('file://' + f, { waitUntil: 'load' });
      const r = await page.evaluate(() => ({ o: document.documentElement.scrollWidth - innerWidth, broken: [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(27, 60)) }));
      if (r.o > 0 || errs.length || r.broken.length) bad.push([vp.width, f.replace('/mnt/user-data/outputs/notaires/', ''), r.o, errs, r.broken]);
    }
    await ctx.close();
  }
  console.log(JSON.stringify(bad, null, 1), '\nchecked', files.length * 2); await b.close();
})();
