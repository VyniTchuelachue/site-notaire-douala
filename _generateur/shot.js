// Captures d'écran locales : sert les Google Fonts depuis @fontsource et remplace la carte Google par un aplat.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const FS = '/root/fonts/node_modules/@fontsource';

function fontCss(url) {
  const u = new URL(url); let css = '';
  for (const fam of u.searchParams.getAll('family')) {
    const [name, spec] = fam.split(':'); const id = name.toLowerCase().replace(/ /g, '-');
    const weights = spec ? spec.replace('wght@', '').split(';') : ['400'];
    for (const w of weights) {
      for (const style of ['normal', 'italic']) {
        const f = path.join(FS, id, 'files', `${id}-latin-${w}-${style}.woff2`);
        if (fs.existsSync(f)) css += `@font-face{font-family:"${name}";font-style:${style};font-weight:${w};src:url(data:font/woff2;base64,${fs.readFileSync(f).toString('base64')}) format("woff2");}\n`;
      }
    }
  }
  return css;
}

(async () => {
  const [,, file, out, mode] = process.argv;
  const browser = await chromium.launch();
  const vp = mode === 'mobile' ? { width: 390, height: 844 } : { width: 1440, height: 900 };
  const ctx = await browser.newContext({ viewport: vp, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  await page.route('https://fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body: fontCss(r.request().url()) }));
  await page.route('https://fonts.gstatic.com/**', r => r.abort());
  await page.route('https://maps.google.com/**', r => r.fulfill({ contentType: 'text/html', body: '<body style="margin:0;background:#dfe6e2;font:14px sans-serif;display:grid;place-items:center;height:100vh;color:#567">Carte Google Maps</body>' }));
  await page.route('https://images.unsplash.com/**', r => { const id = new URL(r.request().url()).pathname.slice(1); const f = '/root/ph/' + id + '.jpg'; return fs.existsSync(f) ? r.fulfill({ contentType: 'image/jpeg', body: fs.readFileSync(f) }) : r.fulfill({ status: 404, body: '' }); });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  await page.goto('file://' + file, { waitUntil: 'load' });
  await page.waitForTimeout(400);
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  await page.screenshot({ path: out, fullPage: true });
  console.log(JSON.stringify({ out, overflow, errors }));
  await browser.close();
})();
