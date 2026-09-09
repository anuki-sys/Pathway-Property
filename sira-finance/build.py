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

import base64
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


def svg_asset(name):
    """Inline an SVG asset, stripped of its XML declaration."""
    svg = read(f"assets/{name}")
    return re.sub(r"<\?xml[^>]*\?>\s*", "", svg).strip()


def data_uri(name, mime):
    return data_uri_path(ROOT / "assets" / name, mime)


MIME = {".webp": "image/webp", ".png": "image/png", ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg", ".svg": "image/svg+xml"}


def inline_images(html):
    """
    Rewrite src="assets/..." to a data URI so every built page stays a single
    self-contained file. In Webflow these become real hosted assets instead.
    """
    def repl(match):
        rel = match.group(1)
        path = ROOT / rel
        if not path.exists():
            raise SystemExit(f"missing image referenced in markup: {rel}")
        mime = MIME.get(path.suffix.lower())
        if not mime:
            raise SystemExit(f"unsupported image type: {rel}")
        return 'src="%s"' % data_uri_path(path, mime)

    return re.sub(r'src="(assets/[^"]+)"', repl, html)


def data_uri_path(path, mime):
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def favicon():
    """The logo mark, cream on forest, as an inline data URI."""
    mark = svg_asset("sira-logo-mark-dark.svg")
    mark = mark.replace("<svg ", '<svg style="background:#154D47" ', 1)
    return "data:image/svg+xml;base64," + base64.b64encode(mark.encode()).decode("ascii")


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

    assets = {
        "{{LOGO_LOCKUP_LIGHT}}": svg_asset("sira-logo-lockup-light.svg"),
        "{{LOGO_LOCKUP_DARK}}": svg_asset("sira-logo-lockup-dark.svg"),
        "{{WAVE_SRC}}": f"url({data_uri('sira-wavy-texture.webp', 'image/webp')})",
        "{{FAVICON}}": favicon(),
    }
    nav = nav.replace("{{LOGO_LOCKUP_LIGHT}}", assets["{{LOGO_LOCKUP_LIGHT}}"])
    footer = footer.replace("{{LOGO_LOCKUP_DARK}}", assets["{{LOGO_LOCKUP_DARK}}"])

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
        ) + tuple(assets.items()):
            html = html.replace(token, value)

        html = inline_images(html)

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
