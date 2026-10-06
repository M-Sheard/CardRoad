#!/usr/bin/env python3
"""Knock the lime chroma off a generated terrain piece and leave a clean alpha.

Same convention the NPC standees use: shoot the piece on #00FF00, key it here.
Greenness is measured as g - max(r, b), which ignores how bright the backdrop
is and only asks how green it is, so olive grass on the base survives while the
flat backdrop does not.
"""

import sys
from pathlib import Path

import numpy as np
from PIL import Image

SOFT_EDGE = 18.0   # greenness at which a pixel is still fully opaque
FULL_KEY = 72.0    # greenness at which a pixel is fully transparent


def key(src: Path, dst: Path) -> None:
    rgb = np.asarray(Image.open(src).convert("RGB"), dtype=np.float32)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]

    greenness = g - np.maximum(r, b)
    alpha = np.clip((FULL_KEY - greenness) / (FULL_KEY - SOFT_EDGE), 0.0, 1.0)

    # Pull the green cast out of the semi-transparent rim so edges don't fringe.
    spill = np.clip(greenness, 0.0, None) * (alpha > 0)
    out = rgb.copy()
    out[..., 1] = g - spill

    composed = np.dstack([np.clip(out, 0, 255), alpha * 255.0]).astype(np.uint8)
    img = Image.fromarray(composed, mode="RGBA")

    bbox = img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        img = img.crop(bbox)

    img.save(dst)
    print(f"{dst.name}  {img.width}x{img.height}")


if __name__ == "__main__":
    here = Path(__file__).parent
    for name in sys.argv[1:]:
        key(Path(name), here / (Path(name).stem + ".png"))
