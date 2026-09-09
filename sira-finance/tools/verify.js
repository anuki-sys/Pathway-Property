/*
 * Interaction and accessibility checks for the built home page.
 *   node tools/verify.js
 * Covers the dropdown nav, scenario picker, comparison switch, process rail,
 * FAQ, slider and call bar, plus the three states that are easy to break:
 * reduced motion, no JavaScript, and a 390px viewport.
 */
const { chromium } = require('playwright');
const URL = 'file:///home/user/Pathway-Property/sira-finance/dist/index.html';
const CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const ok = (l, v) => console.log((v ? 'PASS  ' : 'FAIL  ') + l);

(async () => {
  const b = await chromium.launch({ executablePath: CHROME });

  // --- full interaction pass
  let p = await b.newPage({ viewport: { width: 1440, height: 950 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(URL, { waitUntil: 'networkidle' });
  await p.waitForTimeout(900);

  await p.locator('.nav__item.has-menu').nth(2).hover(); await p.waitForTimeout(350);
  ok('nav dropdown opens on hover', await p.locator('#menu-work').evaluate(e => getComputedStyle(e).opacity) === '1');
  await p.keyboard.press('Escape'); await p.waitForTimeout(250);
  ok('escape closes dropdown', await p.locator('.nav__item.has-menu').nth(2).evaluate(e => !e.classList.contains('is-open')));

  await p.evaluate(() => document.querySelector('[data-picker]').scrollIntoView({block:'center'}));
  await p.waitForTimeout(500);
  await p.locator('[role="tab"]').nth(5).click(); await p.waitForTimeout(450);
  ok('picker swaps panel', (await p.locator('[data-field="title"]').textContent()) === 'Funding a development');
  ok('picker swaps link', (await p.locator('[data-field="primary"]').getAttribute('href')) === '/islamic-finance/development-finance/');
  ok('picker swaps guides', (await p.locator('[data-field="guide2"]').textContent()) === 'Ijarah explained');
  ok('one tab selected', (await p.locator(String.raw`.picker [role="tab"][aria-selected="true"]`).count()) === 1);

  await p.evaluate(() => document.querySelector('[data-compare]').scrollIntoView({block:'center'}));
  await p.waitForTimeout(400);
  await p.locator('.switch button').nth(1).click(); await p.waitForTimeout(400);
  ok('switch swaps rows', (await p.locator('.compare__row dd').first().textContent()).startsWith('A broker'));
  await p.locator('.switch button').nth(0).click(); await p.waitForTimeout(400);
  ok('switch swaps back', (await p.locator('.compare__row dd').first().textContent()).startsWith('One provider'));

  await p.evaluate(() => document.querySelector('.steps').scrollIntoView({block:'center'}));
  await p.waitForTimeout(500);
  const w = parseFloat(await p.locator('.steps-rail__fill').evaluate(e => e.style.width));
  ok('process rail fills (' + w.toFixed(0) + '%)', w > 10 && w < 100);

  await p.locator('.faq__item summary').first().click(); await p.waitForTimeout(550);
  ok('faq animates open', await p.locator('.faq__item').first().evaluate(e => e.open));
  await p.locator('[data-slider="next"]').click(); await p.waitForTimeout(550);
  ok('slider advances', (await p.locator('.slider__track').evaluate(e => e.style.transform)) !== 'translateX(0px)');

  for (let y = 0; y < 11000; y += 650) { await p.evaluate(v => scrollTo(0, v), y); await p.waitForTimeout(90); }
  await p.waitForTimeout(1200);
  ok('nothing left hidden', (await p.evaluate(() => [...document.querySelectorAll('.reveal,.stagger>*,.media img')].filter(e => parseFloat(getComputedStyle(e).opacity) < 0.99).length)) === 0);
  ok('no page errors', errs.length === 0);
  if (errs.length) console.log(errs);
  await p.close();

  // --- reduced motion
  let ctx = await b.newContext({ reducedMotion: 'reduce', viewport: { width: 1440, height: 950 } });
  p = await ctx.newPage();
  await p.goto(URL, { waitUntil: 'networkidle' }); await p.waitForTimeout(700);
  ok('reduced motion: nothing hidden', (await p.evaluate(() => [...document.querySelectorAll('.reveal,.stagger>*,.media img')].filter(e => parseFloat(getComputedStyle(e).opacity) < 0.99).length)) === 0);
  ok('reduced motion: drift off', (await p.evaluate(() => getComputedStyle(document.querySelector('.has-wave'), '::before').animationName)) === 'none');
  await p.locator('[role="tab"]').nth(2).click(); await p.waitForTimeout(200);
  ok('reduced motion: picker still swaps', (await p.locator('[data-field="title"]').textContent()) === 'Buying an investment property');
  await ctx.close();

  // --- no javascript
  ctx = await b.newContext({ javaScriptEnabled: false, viewport: { width: 1440, height: 950 } });
  p = await ctx.newPage();
  await p.goto(URL, { waitUntil: 'load' }); await p.waitForTimeout(400);
  ok('no-js: content visible', (await p.locator('.section-head h2').first().isVisible()));
  ok('no-js: nav links reachable', (await p.locator('#menu-finance .nav__entry').first().isVisible()));
  await ctx.close();

  // --- mobile
  p = await b.newPage({ viewport: { width: 390, height: 844 } });
  await p.goto(URL, { waitUntil: 'networkidle' }); await p.waitForTimeout(700);
  ok('mobile: no overflow', (await p.evaluate(() => document.documentElement.scrollWidth)) === 390);
  await p.locator('.nav-toggle').click(); await p.waitForTimeout(300);
  await p.locator('.nav__link').nth(1).click(); await p.waitForTimeout(400);
  ok('mobile: submenu expands', parseInt(await p.locator('#menu-finance').evaluate(e => e.style.height)) > 100);
  await p.locator('.nav-toggle').click(); await p.waitForTimeout(300);
  await p.evaluate(() => scrollTo(0, 2500)); await p.waitForTimeout(500);
  ok('mobile: call bar appears', await p.locator('.callbar').evaluate(e => e.classList.contains('is-up')));
  await b.close();
})();
