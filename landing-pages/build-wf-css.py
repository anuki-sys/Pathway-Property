#!/usr/bin/env python3
"""Derive the Webflow stylesheet from the source page.

Two transforms, and only two: drop the nav rules (on Webflow the real navbar
component replaces the stand-in) and drop body's padding-top (the component
carries its own offset). Everything else is copied byte for byte, so a diff
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
open(sys.argv[2], 'w').write(o)
print(f'dropped {dropped} nav rules, {len(o)} bytes')
