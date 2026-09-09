#!/usr/bin/env python3
"""
Generate branded image placeholders for the review build.

There is no photography yet. Rather than leave empty boxes or drop in stock
images that would have to be torn out later, every image slot gets a calm,
on-brand placeholder at the exact aspect ratio the real photograph needs.
Swapping in the real shot is then a one-line src change and nothing reflows.

Each placeholder is a different crop of the wavy silk from the logo artwork,
toned to a warm stone. Stone rather than brand green on purpose: these sit on
both cream and green surfaces, and a green placeholder disappears into the
green ones. Warm neutral also sits closer to what the real photographs will
be, so the page balance does not shift when they land.
"""

import pathlib

from PIL import Image, ImageEnhance, ImageFilter

ROOT = pathlib.Path(__file__).parent.parent
SRC = ROOT / "assets" / "sira-wavy-texture.webp"
OUT = ROOT / "assets" / "placeholders"

# Warm stone, a little darker for the wide slots so they read against cream.
STONE = (150, 141, 128)
STONE_DEEP = (122, 115, 104)

# name, width, height, crop anchor (0-1 across the source), base tone
SLOTS = [
    ("hero-portrait", 900, 1200, (0.62, 0.30), STONE),
    ("support-wide", 1200, 860, (0.30, 0.62), STONE_DEEP),
    ("process-wide", 1400, 620, (0.50, 0.20), STONE),
    ("video-poster", 1280, 800, (0.20, 0.45), STONE_DEEP),
    ("team-1", 640, 800, (0.15, 0.20), STONE),
    ("team-2", 640, 800, (0.50, 0.55), STONE),
    ("team-3", 640, 800, (0.82, 0.35), STONE),
]


def crop_to(im, w, h, anchor):
    """Cover-crop the source to the target ratio around an anchor point."""
    target = w / h
    sw, sh = im.size
    if sw / sh > target:
        cw, ch = int(sh * target), sh
    else:
        cw, ch = sw, int(sw / target)
    ax, ay = anchor
    left = max(0, min(sw - cw, int(ax * sw - cw / 2)))
    top = max(0, min(sh - ch, int(ay * sh - ch / 2)))
    return im.crop((left, top, left + cw, top + ch)).resize((w, h), Image.LANCZOS)


def tint(im, colour):
    """
    Tone the greyscale silk to a warm neutral. The contrast is pulled right
    down so the pattern reads as texture, not as a picture of something.
    """
    grey = im.convert("L")
    grey = ImageEnhance.Contrast(grey).enhance(0.55)
    lift = 58  # how far highlights travel above the base tone
    return Image.merge("RGB", [
        grey.point(lambda v, c=c: min(255, int(c + (v / 255) * lift)))
        for c in colour
    ])


def main():
    if not SRC.exists():
        raise SystemExit(f"missing {SRC}. Run tools/extract_brand_assets.py first.")
    OUT.mkdir(parents=True, exist_ok=True)
    base = Image.open(SRC).convert("RGB")

    for name, w, h, anchor, colour in SLOTS:
        im = tint(crop_to(base, w, h, anchor), colour)
        im = im.filter(ImageFilter.GaussianBlur(1.4))
        path = OUT / f"sira-placeholder-{name}.webp"
        im.save(path, "WEBP", quality=76, method=6)
        print(f"  {path.name:<40} {w}x{h}  {path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
