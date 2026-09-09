#!/usr/bin/env python3
"""
Derive the brand assets from the supplied logo artwork.

Input:  brand/source/sira-logo-wavy.pdf
Output: assets/
          sira-logo-lockup-dark.svg   cream lockup, for green backgrounds
          sira-logo-lockup-light.svg  green mark and ink wordmark, for cream
          sira-logo-mark-dark.svg     mark only, cream
          sira-logo-mark-light.svg    mark only, green
          sira-wavy-texture.webp      the silk texture behind the logo

The lockup is the real vector art lifted out of the supplied file, not a
redraw. The two variants differ only by fill colour: the wordmark glyphs
carry #faf8f5 and the mark paths carry #f5f2eb in the source, so each can be
recoloured independently without touching the geometry.

The mark reads as a cream square with a sail curved out of it. That curve is
negative space, so on a cream page the whole path is filled green instead and
the page shows through as the sail.
"""

import pathlib
import re

import pymupdf
from PIL import Image

ROOT = pathlib.Path(__file__).parent.parent
SRC = ROOT / "brand" / "source" / "sira-logo-wavy.pdf"
OUT = ROOT / "assets"

# Measured from the source artwork, in PDF points.
LOCKUP = pymupdf.Rect(58.6, 125.0, 314.6, 241.9)
MARK = pymupdf.Rect(58.6, 150.7, 138.8, 230.9)
PAD = 2

# Fills as they appear in the source.
WORDMARK_FILL = "#faf8f5"
MARK_FILL = "#f5f2eb"

# Brand colours sampled from the artwork.
CREAM = "#F5F1EB"
FOREST = "#154D47"
INK = "#0A1C1A"


def vector_svg(box):
    """Crop the page to box and return SVG with the raster ground removed."""
    doc = pymupdf.open(SRC)
    page = doc[0]
    page.set_cropbox(pymupdf.Rect(box.x0 - PAD, box.y0 - PAD, box.x1 + PAD, box.y1 + PAD))
    svg = page.get_svg_image()
    svg = re.sub(r"<image\b[^>]*?/>", "", svg, flags=re.DOTALL)
    svg = re.sub(r"<image\b.*?</image>", "", svg, flags=re.DOTALL)
    # The white page rect sat under the raster and would otherwise show through.
    svg = re.sub(r'<path[^>]*fill="#ffffff"[^>]*/>', "", svg)
    return svg


def recolour(svg, mark, wordmark):
    svg = svg.replace(MARK_FILL, mark)
    # The macron over the i is a stroke, not a fill, so replace the raw value.
    return svg.replace(WORDMARK_FILL, wordmark)


def write(name, svg):
    path = OUT / name
    path.write_text(svg, encoding="utf-8")
    print(f"  {name}  {path.stat().st_size // 1024} KB")


def main():
    if not SRC.exists():
        raise SystemExit(f"missing {SRC}")
    OUT.mkdir(exist_ok=True)

    print("logo:")
    lockup = vector_svg(LOCKUP)
    write("sira-logo-lockup-dark.svg", recolour(lockup, CREAM, "#FAF8F5"))
    write("sira-logo-lockup-light.svg", recolour(lockup, FOREST, INK))

    mark = vector_svg(MARK)
    write("sira-logo-mark-dark.svg", recolour(mark, CREAM, CREAM))
    write("sira-logo-mark-light.svg", recolour(mark, FOREST, FOREST))

    print("texture:")
    doc = pymupdf.open(SRC)
    xref = doc[0].get_images()[0][0]
    raw = doc.extract_image(xref)
    tmp = OUT / f"_wavy.{raw['ext']}"
    tmp.write_bytes(raw["image"])
    im = Image.open(tmp).convert("RGB")
    im.thumbnail((1400, 1400), Image.LANCZOS)
    im.save(OUT / "sira-wavy-texture.webp", "WEBP", quality=82, method=6)
    tmp.unlink()
    print(f"  sira-wavy-texture.webp  {im.size[0]}x{im.size[1]}  "
          f"{(OUT / 'sira-wavy-texture.webp').stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
