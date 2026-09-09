#!/usr/bin/env python3
"""
Check every built page against the non-negotiable copy rules in
00-BUILD-INSTRUCTIONS.md section 2. Run after build.py.

Exits non-zero if anything fails, so it can gate a build later.
"""

import pathlib
import re
import sys

DIST = pathlib.Path(__file__).parent.parent / "dist"

# Strip tags, scripts, styles and HTML comments before checking prose.
STRIP = re.compile(
    r"<script.*?</script>|<style.*?</style>|<!--.*?-->|<[^>]+>", re.DOTALL | re.IGNORECASE
)

BANNED_WORDS = [
    # (pattern, message, allowed-context pattern or None)
    (r"\bloans?\b", 'say "finance", never "loan"', r"home loan"),
    (r"\blending\b", 'say "finance", never "lending"', None),
    (r"\blenders?\b", 'say "funder", never "lender"', None),
    (r"\bborrow(?:er|ing|ers)?\b", 'say "finance", never "borrow"', None),
    (r"\bmortgages?\b", '"mortgage" is only allowed in "mortgage manager"', r"mortgage manager"),
    (r"\bhalal (?:loan|finance|mortgage)\b", "never claim a product is halal", None),
]

SUPERLATIVES = [
    r"\bAustralia'?s top\b", r"\bnumber 1\b", r"\bno\.? ?1\b", r"\bbiggest\b",
    r"\bbest in\b", r"\bleading\b", r"\bAussie'?s top\b", r"\bthe largest\b",
]

AMERICANISMS = [
    (r"\borgani[sz]ation\b", "organisation"), (r"\brecogniz", "recognise"),
    (r"\bcenter\b", "centre"), (r"\bcolor\b", "colour"), (r"\blicense\b", "licence (noun)"),
    (r"\bcustomiz", "customise"), (r"\banaly[z]e", "analyse"),
]


def check(path):
    html = path.read_text(encoding="utf-8")
    problems = []

    # The <head> counts for dashes and meta length; prose rules run on visible text only.
    text = STRIP.sub(" ", html)
    text = re.sub(r"\s+", " ", text)

    for ch, name in (("—", "em dash"), ("–", "en dash")):
        if ch in html:
            problems.append(f"{name} found. Regular hyphens only.")

    for pattern, message, allowed in BANNED_WORDS:
        probe = text
        if allowed:
            probe = re.sub(allowed, " ", probe, flags=re.IGNORECASE)
        for hit in set(m.group(0) for m in re.finditer(pattern, probe, re.IGNORECASE)):
            problems.append(f'banned word "{hit}": {message}')

    for pattern in SUPERLATIVES:
        for hit in set(m.group(0) for m in re.finditer(pattern, text, re.IGNORECASE)):
            problems.append(f'superlative "{hit}" is banned')

    for pattern, correct in AMERICANISMS:
        for hit in set(m.group(0) for m in re.finditer(pattern, text, re.IGNORECASE)):
            problems.append(f'US spelling "{hit}", use "{correct}"')

    # No ALL CAPS words of three letters or more, excluding known acronyms.
    acronyms = {
        "ABN", "ACL", "AFCA", "NCCP", "AUD", "SMSF", "LMI", "FAQ", "CTA", "SEO",
        "AU", "VIC", "NSW", "WA", "QLD", "SA", "TAS", "NT", "ACT", "GST", "CMS",
    }
    for hit in set(re.findall(r"\b[A-Z]{3,}\b", text)):
        if hit not in acronyms:
            problems.append(f'ALL CAPS "{hit}". Sentence case everywhere.')

    # Meta length
    title = re.search(r"<title>(.*?)</title>", html, re.DOTALL)
    desc = re.search(r'<meta name="description" content="(.*?)"', html, re.DOTALL)
    if title and len(title.group(1)) > 60:
        problems.append(f"meta title is {len(title.group(1))} chars, limit is 60")
    if desc and len(desc.group(1)) > 155:
        problems.append(f"meta description is {len(desc.group(1))} chars, limit is 155")
    if not desc or not desc.group(1).strip():
        problems.append("missing meta description")

    # Every image needs alt text.
    for img in re.finditer(r"<img\b[^>]*>", html, re.IGNORECASE):
        if "alt=" not in img.group(0):
            problems.append("image without alt text")

    return problems


def main():
    pages = sorted(DIST.rglob("*.html"))
    if not pages:
        sys.exit("No built pages found. Run build.py first.")

    failed = 0
    for page in pages:
        problems = check(page)
        rel = page.relative_to(DIST)
        if problems:
            failed += 1
            print(f"\n{rel}")
            for p in sorted(set(problems)):
                print(f"  - {p}")
        else:
            print(f"{rel}: clean")

    print(f"\n{len(pages) - failed}/{len(pages)} page(s) clean")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
