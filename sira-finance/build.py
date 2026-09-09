#!/usr/bin/env python3
"""
Build the Sira Finance static review site from src/.

Each page in src/pages/ starts with an HTML comment holding its metadata:

    <!--meta
    { "path": "...", "title": "...", "description": "...", "schema": "home" }
    -->

The shared CSS is inlined into every output page so any single file can be
opened, emailed or previewed on its own with no broken references.
"""

import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

META_RE = re.compile(r"<!--meta\s*(\{.*?\})\s*-->", re.DOTALL)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def schema_block(name):
    if not name:
        return ""
    data = json.loads(read(f"schema/{name}.json"))
    blocks = data if isinstance(data, list) else [data]
    return "\n".join(
        '<script type="application/ld+json">\n%s\n</script>'
        % json.dumps(b, indent=2, ensure_ascii=False)
        for b in blocks
    )


def main():
    layout = read("src/layout.html")
    css = read("css/sira.css")
    fonts = read("css/fonts.css")
    nav = read("src/partials/nav.html")
    footer = read("src/partials/footer.html")
    draftbar = read("src/partials/draftbar.html")

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    built = []
    for page in sorted((SRC / "pages").glob("*.html")):
        raw = page.read_text(encoding="utf-8")
        match = META_RE.search(raw)
        if not match:
            raise SystemExit(f"{page.name}: missing <!--meta ... --> block")
        meta = json.loads(match.group(1))
        body = META_RE.sub("", raw, count=1).strip()

        html = layout
        for token, value in (
            ("{{TITLE}}", meta["title"]),
            ("{{DESCRIPTION}}", meta["description"]),
            ("{{FONTS}}", fonts),
            ("{{CSS}}", css),
            ("{{SCHEMA}}", schema_block(meta.get("schema"))),
            ("{{DRAFTBAR}}", draftbar),
            ("{{NAV}}", nav),
            ("{{FOOTER}}", footer),
            ("{{BODY}}", body),
        ):
            html = html.replace(token, value)

        out = DIST / meta["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        built.append((meta["path"], len(meta["title"]), len(meta["description"])))

    print(f"Built {len(built)} page(s) into dist/")
    for path, t, d in built:
        flag_t = " TITLE OVER 60" if t > 60 else ""
        flag_d = " DESCRIPTION OVER 155" if d > 155 else ""
        print(f"  {path:<40} title {t:>3}  description {d:>3}{flag_t}{flag_d}")


if __name__ == "__main__":
    main()
