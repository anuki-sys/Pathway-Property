/*
 * Screenshot a built page for review.
 *   node tools/screenshot.js dist/index.html /tmp/out
 * Writes <out>-desktop.png (1440 full page) and <out>-mobile.png (390 full page).
 * Uses the pre-installed Chromium rather than downloading one.
 */
const { chromium } = require('playwright');

const CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

(async () => {
  const [file, out] = process.argv.slice(2);
  if (!file || !out) {
    console.error('usage: node tools/screenshot.js <html file> <output prefix>');
    process.exit(1);
  }
  const browser = await chromium.launch({ executablePath: CHROME });
  for (const [name, width, height] of [['desktop', 1440, 900], ['mobile', 390, 844]]) {
    const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 2 });
    await page.goto('file://' + require('path').resolve(file), { waitUntil: 'networkidle' });
    // Settle the scroll reveals so the full-page capture is not half faded out.
    await page.evaluate(() => document.querySelectorAll('.reveal').forEach(e => e.classList.add('is-in')));
    await page.waitForTimeout(600);
    await page.screenshot({ path: `${out}-${name}.png`, fullPage: true });
    await page.close();
  }
  await browser.close();
  console.log(`wrote ${out}-desktop.png and ${out}-mobile.png`);
})();
