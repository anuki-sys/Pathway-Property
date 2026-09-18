#!/usr/bin/env python3
"""Derive the Webflow CSS and JS assets from the source page.

    python3 build-wf-assets.py buyers-agent-melbourne.html <out-dir>

writes melbourne-page.css and melbourne-page.js. The CSS gets two transforms,
and only two: drop the nav rules (on Webflow the real navbar component replaces
the stand-in) and drop body's padding-top (the component carries its own
offset). The JS is copied verbatim. Everything else is byte for byte, so a diff
against the previously served file only ever shows a real change."""
import re, sys
NAV = re.compile(r'\.navbar|\.nav-item|\.nav-toggle|\.nav-dropdown|\.nav-trigger'
                 r'|\.nav-enquire|\.text-logo|\.logo-mark|\.caret|\.dd-note|\.dd-soon'
                 r'|\.dd-sub|\.has-menu|aria-expanded')

def rules(s, base=0):
    """Yield (start, end) of each top-level rule in s, as offsets into the parent."""
    depth = start = 0
    for i, c in enumerate(s):
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                yield base + start, base + i + 1
                start = i + 1

src = open(sys.argv[1]).read()
out_dir = sys.argv[2].rstrip('/')
css = src.split('<style>', 1)[1].split('</style>', 1)[0]

cut = []      # byte ranges to remove
dropped = 0
for a, b in rules(css):
    chunk = css[a:b]
    sel = chunk.split('{', 1)[0]
    if sel.lstrip().startswith('@media'):
        inner_a = a + chunk.index('{') + 1
        inner_b = a + chunk.rindex('}')
        subs = list(rules(css[inner_a:inner_b], inner_a))
        navs = [(x, y) for x, y in subs if NAV.search(css[x:y].split('{', 1)[0])]
        if not navs:
            continue
        dropped += len(navs)
        cut.append((a, b) if len(navs) == len(subs) else None) or cut.extend(navs)
        continue
    if NAV.search(sel):
        dropped += 1
        cut.append((a, b))

out, prev = [], 0
for a, b in sorted(x for x in cut if x):
    if a < prev:
        continue
    out.append(css[prev:a]); prev = b
out.append(css[prev:])
o = re.sub(r'\n?\s*padding-top:104px;?', '', ''.join(out))
open(f'{out_dir}/melbourne-page.css', 'w').write(o)
print(f'css: dropped {dropped} nav rules, {len(o)} bytes')

# The page's last <script> block is the whole behaviour layer. The nav IIFE
# inside it stays: it guards on the stand-in's elements being absent, which on
# Webflow they are, and without that guard every later IIFE in the file dies.
js = src.rsplit('<script>', 1)[1].split('</script>', 1)[0]
open(f'{out_dir}/melbourne-page.js', 'w').write(js)
print(f'js: {len(js)} bytes')
