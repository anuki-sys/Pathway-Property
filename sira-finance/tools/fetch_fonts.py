#!/usr/bin/env python3
"""
Self-host Plus Jakarta Sans for the review build.

The sandboxed browser cannot reach fonts.googleapis.com, and a review build
that is emailed around should not depend on a CDN either. This fetches the
latin subset of each variable font and writes css/fonts.css with the font
bytes inlined as data URIs, so every built page is self-contained.

In Webflow it is a native Google font and is already enabled on the site,
so none of this ships to production.
"""

import base64
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).parent.parent
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")

# Plus Jakarta Sans is the typeface in the logo artwork and the only family on
# the current site. ExtraLight through Bold, because the logo lockup itself
# pairs SemiBold "sira" with ExtraLight "finance" and the site reuses that.
FAMILIES = [
    ("Plus Jakarta Sans", "Plus+Jakarta+Sans:wght@200..800"),
]

FACE_RE = re.compile(r"/\*\s*(\S+)\s*\*/\s*(@font-face\s*\{.*?\})", re.DOTALL)


def curl(url, binary=False):
    out = subprocess.run(
        ["curl", "-sSfL", "-A", UA, url], capture_output=True, check=True
    ).stdout
    return out if binary else out.decode("utf-8")


def main():
    chunks = ["/* Self-hosted for the review build only. Webflow uses the native Google fonts. */"]
    for name, spec in FAMILIES:
        css = curl(f"https://fonts.googleapis.com/css2?family={spec}&display=swap")
        kept = 0
        for subset, block in FACE_RE.findall(css):
            if subset != "latin":
                continue
            url_match = re.search(r"url\((https://[^)]+\.woff2)\)", block)
            if not url_match:
                continue
            data = curl(url_match.group(1), binary=True)
            b64 = base64.b64encode(data).decode("ascii")
            block = block.replace(
                url_match.group(0),
                f"url(data:font/woff2;base64,{b64})",
            )
            chunks.append(block)
            kept += 1
            print(f"{name} latin: {len(data) // 1024} KB inlined")
        if not kept:
            raise SystemExit(f"{name}: no latin face found")

    out = ROOT / "css" / "fonts.css"
    out.write_text("\n\n".join(chunks) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
