#!/usr/bin/env python3
"""Resize a card painting to 720x1280 and write live WebP q80."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

LIVE = (720, 1280)


def cover_resize(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    tw, th = size
    iw, ih = im.size
    scale = max(tw / iw, th / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    x, y = (nw - tw) // 2, (nh - th) // 2
    return im.crop((x, y, x + tw, y + th))


def convert(src: Path, dest_webp: Path) -> int:
    im = Image.open(src).convert("RGB")
    live = cover_resize(im, LIVE)
    dest_webp.parent.mkdir(parents=True, exist_ok=True)
    live.save(dest_webp, format="WEBP", quality=80, method=6)
    return dest_webp.stat().st_size


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("id", help="C001")
    p.add_argument("--assets", default="/workspace/assets/cards")
    args = p.parse_args()
    dest = Path(args.assets) / f"{args.id}.webp"
    n = convert(Path(args.src), dest)
    print(f"{args.id} {n} {dest}")


if __name__ == "__main__":
    main()
