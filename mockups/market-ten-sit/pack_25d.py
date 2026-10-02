#!/usr/bin/env python3
"""2.5D market sit: extract furniture from the paintings, unique people blocking."""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ART = Path("/opt/cursor/artifacts/assets")
OUT = Path("/workspace/mockups/market-ten-sit")
NPC = Path("/workspace/mockups")
DBG = Path("/tmp/market-sit/debug-masks")
OUT.mkdir(parents=True, exist_ok=True)
DBG.mkdir(parents=True, exist_ok=True)

W, H = 720, 1280

SCENES = [
    ("sit-01-felt-aisle", "01 Facing felt stalls"),
    ("sit-02-stall-sign", "02 Stall and gilt sign"),
    ("sit-03-warm-cross", "03 Market cross"),
    ("sit-04-mill-yard", "04 Mill yard"),
    ("sit-05-oak-hall", "05 Oak hall"),
    ("sit-06-oak-tree-stall", "06 Oak tree and stall"),
    ("sit-07-warm-quay", "07 Warm quay"),
    ("sit-08-inn-yard", "08 Inn yard"),
    ("sit-09-club-portico", "09 Club portico"),
    ("sit-10-felt-table", "10 Felt card table"),
]

# Furniture: (z, {polys, ellipses}). z=2 mid, z=4 near.
# People z=1 behind mid, z=3 between, z=5 in front.
OBJECTS = {
    "sit-01-felt-aisle": [
        (2, {"polys": [[(0, 640), (275, 638), (288, 665), (278, 880), (40, 915), (0, 900)]]}),
        (2, {"polys": [[(500, 618), (720, 618), (720, 905), (492, 918), (488, 645)]]}),
    ],
    "sit-02-stall-sign": [
        (2, {"polys": [[(0, 648), (328, 648), (348, 675), (338, 882), (0, 892)]]}),
        (4, {"ellipses": [(558, 672, 718, 902)]}),
    ],
    "sit-03-warm-cross": [
        (2, {"polys": [
            [(98, 305), (158, 298), (168, 698), (92, 722)],
            [(298, 298), (358, 292), (365, 688), (288, 712)],
        ]}),
        (2, {"polys": [[(498, 652), (720, 638), (720, 805), (488, 818), (485, 675)]]}),
    ],
    "sit-04-mill-yard": [
        (2, {"polys": [[(0, 598), (358, 598), (378, 628), (368, 792), (42, 805), (0, 788)]]}),
        (4, {"ellipses": [(478, 655, 718, 858)]}),
    ],
    "sit-05-oak-hall": [
        (2, {"polys": [[(12, 698), (388, 688), (408, 718), (398, 892), (38, 905), (8, 860)]]}),
    ],
    "sit-06-oak-tree-stall": [
        (2, {"polys": [[(0, 380), (140, 370), (200, 450), (188, 580), (175, 700), (140, 790), (40, 810), (0, 780)]]}),
        (2, {"polys": [[(498, 668), (720, 655), (720, 782), (488, 795), (482, 690)]]}),
    ],
    "sit-07-warm-quay": [
        (2, {"polys": [[(0, 598), (338, 598), (358, 628), (348, 838), (0, 850)]]}),
        (4, {"polys": [[(32, 908), (248, 892), (288, 922), (276, 1178), (18, 1188), (12, 948)]]}),
    ],
    "sit-08-inn-yard": [
        (2, {"polys": [[(50, 488), (74, 482), (80, 792), (46, 802)]]}),
        (2, {"polys": [[(498, 652), (705, 638), (722, 675), (712, 782), (488, 792)]]}),
    ],
    "sit-09-club-portico": [
        (2, {"polys": [[(18, 618), (358, 612), (375, 640), (365, 822), (12, 832)]]}),
        (2, {"polys": [[(598, 70), (720, 70), (720, 720), (588, 742), (582, 180)]]}),
    ],
    "sit-10-felt-table": [
        (2, {"polys": [[(498, 598), (720, 575), (720, 772), (478, 785), (472, 640)]]}),
        (4, {"polys": [[(58, 648), (348, 642), (362, 675), (350, 848), (62, 852)]]}),
    ],
}

# (name, fx, fy, hfrac, z) — unique blocking per screen; z=1 behind, 3 between, 5 in front
PEOPLE = {
    # Open aisle: vendors in both stalls, shoppers on opposite sides, centre path clear.
    "sit-01-felt-aisle": [
        ("tomas", 0.18, 0.70, 0.32, 1),
        ("bram", 0.86, 0.70, 0.30, 1),
        ("elira", 0.34, 0.78, 0.28, 3),
        ("nessa", 0.70, 0.92, 0.36, 5),
    ],
    # Shopper close-left at the stall; Nessa behind the barrel; Elira far up the street.
    "sit-02-stall-sign": [
        ("tomas", 0.20, 0.69, 0.30, 1),
        ("elira", 0.58, 0.56, 0.18, 1),
        ("nessa", 0.88, 0.70, 0.26, 3),
        ("bram", 0.32, 0.94, 0.40, 5),
    ],
    # Talk on the square (mid-right). Elira in the gazebo. Empty lower-left.
    "sit-03-warm-cross": [
        ("elira", 0.28, 0.55, 0.22, 1),
        ("tomas", 0.84, 0.63, 0.26, 1),
        ("nessa", 0.40, 0.84, 0.32, 3),
        ("bram", 0.60, 0.92, 0.38, 5),
    ],
    # Bram walks in front of the fruit stall. Nessa behind the millstone. Elira in the mill door.
    "sit-04-mill-yard": [
        ("elira", 0.58, 0.52, 0.20, 1),
        ("tomas", 0.22, 0.62, 0.28, 1),
        ("nessa", 0.82, 0.67, 0.26, 3),
        ("bram", 0.22, 0.96, 0.42, 5),
    ],
    # Nessa talks to Bram at the sideboard. Tomas walks toward the arch. No giant front pair.
    "sit-05-oak-hall": [
        ("elira", 0.82, 0.62, 0.22, 1),
        ("bram", 0.24, 0.70, 0.28, 1),
        ("nessa", 0.38, 0.82, 0.32, 5),
        ("tomas", 0.68, 0.78, 0.30, 5),
    ],
    # Tomas tucked behind the oak. Pair walking right toward the stall.
    "sit-06-oak-tree-stall": [
        ("tomas", 0.26, 0.70, 0.34, 1),
        ("bram", 0.84, 0.61, 0.24, 1),
        ("elira", 0.46, 0.76, 0.26, 3),
        ("nessa", 0.66, 0.88, 0.34, 5),
    ],
    # Nessa behind the crate. Tomas on the quay edge. Elira further down the water.
    "sit-07-warm-quay": [
        ("elira", 0.64, 0.56, 0.18, 1),
        ("bram", 0.18, 0.66, 0.28, 1),
        ("nessa", 0.22, 0.92, 0.36, 3),
        ("tomas", 0.88, 0.94, 0.42, 5),
    ],
    # Tomas behind the lamp. Nessa walking toward the inn. Empty lower-centre.
    "sit-08-inn-yard": [
        ("elira", 0.50, 0.58, 0.20, 1),
        ("bram", 0.84, 0.61, 0.24, 1),
        ("tomas", 0.18, 0.82, 0.38, 1),
        ("nessa", 0.58, 0.86, 0.34, 5),
    ],
    # Tomas at the stall. Nessa entering right. Gap in the middle shows the portico.
    "sit-09-club-portico": [
        ("elira", 0.76, 0.64, 0.26, 1),
        ("bram", 0.24, 0.64, 0.28, 1),
        ("tomas", 0.30, 0.92, 0.40, 5),
        ("nessa", 0.88, 0.86, 0.34, 5),
    ],
    # Tomas at the card table. Nessa entering from the right. Empty lower-left.
    "sit-10-felt-table": [
        ("elira", 0.50, 0.58, 0.20, 1),
        ("bram", 0.84, 0.60, 0.24, 1),
        ("tomas", 0.26, 0.67, 0.30, 3),
        ("nessa", 0.82, 0.94, 0.42, 5),
    ],
}

PADS = {
    "sit-01-felt-aisle": [
        (0.70, 0.92, 0.36),
        (0.34, 0.78, 0.28),
        (0.18, 0.70, 0.32),
        (0.86, 0.70, 0.30),
        (0.50, 0.64, 0.22),
    ],
    "sit-02-stall-sign": [
        (0.32, 0.94, 0.40),
        (0.88, 0.70, 0.26),
        (0.20, 0.69, 0.30),
        (0.58, 0.56, 0.18),
        (0.70, 0.84, 0.28),
    ],
    "sit-03-warm-cross": [
        (0.60, 0.92, 0.38),
        (0.40, 0.84, 0.32),
        (0.84, 0.63, 0.26),
        (0.28, 0.55, 0.22),
        (0.22, 0.96, 0.42),
    ],
    "sit-04-mill-yard": [
        (0.22, 0.96, 0.42),
        (0.82, 0.67, 0.26),
        (0.22, 0.62, 0.28),
        (0.58, 0.52, 0.20),
        (0.50, 0.86, 0.30),
    ],
    "sit-05-oak-hall": [
        (0.38, 0.82, 0.32),
        (0.68, 0.78, 0.30),
        (0.24, 0.70, 0.28),
        (0.82, 0.62, 0.22),
        (0.54, 0.96, 0.40),
    ],
    "sit-06-oak-tree-stall": [
        (0.66, 0.88, 0.34),
        (0.26, 0.70, 0.34),
        (0.46, 0.76, 0.26),
        (0.84, 0.61, 0.24),
        (0.36, 0.96, 0.42),
    ],
    "sit-07-warm-quay": [
        (0.88, 0.94, 0.42),
        (0.22, 0.92, 0.36),
        (0.18, 0.66, 0.28),
        (0.64, 0.56, 0.18),
        (0.52, 0.80, 0.26),
    ],
    "sit-08-inn-yard": [
        (0.58, 0.86, 0.34),
        (0.18, 0.82, 0.38),
        (0.84, 0.61, 0.24),
        (0.50, 0.58, 0.20),
        (0.36, 0.96, 0.42),
    ],
    "sit-09-club-portico": [
        (0.30, 0.92, 0.40),
        (0.88, 0.86, 0.34),
        (0.24, 0.64, 0.28),
        (0.76, 0.64, 0.26),
        (0.56, 0.96, 0.38),
    ],
    "sit-10-felt-table": [
        (0.82, 0.94, 0.42),
        (0.26, 0.67, 0.30),
        (0.84, 0.60, 0.24),
        (0.50, 0.58, 0.20),
        (0.42, 0.90, 0.32),
    ],
}


def font(size: int):
    for p in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def knock_chroma(im: Image.Image) -> Image.Image:
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a and g > 160 and g > r + 40 and g > b + 40:
                px[x, y] = (0, 0, 0, 0)
    return im


def load_npc(name: str) -> Image.Image:
    im = Image.open(NPC / f"{name}_standee_bevel_v19.png").convert("RGBA")
    im = knock_chroma(im)
    im = im.crop(im.getbbox())
    mask = im.getchannel("A")
    warm = Image.new("RGBA", im.size, (210, 168, 110, 28))
    warm.putalpha(mask.point(lambda a: int(a * 0.12) if a else 0))
    im = Image.alpha_composite(im, warm)
    return ImageEnhance.Color(im).enhance(0.96)


NPCS = {n: load_npc(n) for n in ("tomas", "nessa", "bram", "elira")}


def mask_from_spec(spec: dict) -> Image.Image:
    m = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(m)
    for poly in spec.get("polys") or []:
        d.polygon(poly, fill=255)
    for box in spec.get("ellipses") or []:
        d.ellipse(box, fill=255)
    return m.filter(ImageFilter.GaussianBlur(radius=1.2))


def extract_object(bg: Image.Image, spec: dict) -> Image.Image:
    cut = bg.convert("RGBA")
    cut.putalpha(mask_from_spec(spec))
    return cut


def place_standee(canvas: Image.Image, npc: Image.Image, fx: float, fy: float, hfrac: float) -> None:
    target_h = int(H * hfrac)
    tw = max(1, int(npc.width * (target_h / npc.height)))
    sprite = npc.resize((tw, target_h), Image.Resampling.LANCZOS)
    cx, by = int(W * fx), int(H * fy)
    x, y = cx - tw // 2, by - target_h
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(shadow)
    rw, rh = int(tw * 0.38), int(max(10, target_h * 0.045))
    sy = by - int(target_h * 0.035)
    d.ellipse([cx - rw, sy - rh, cx + rw, sy + rh], fill=(52, 32, 16, 120))
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(radius=7)))
    canvas.alpha_composite(sprite, (x, y))


def draw_pads(bg: Image.Image, pads) -> Image.Image:
    out = bg.convert("RGBA")
    overlay = Image.new("RGBA", out.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    f = font(28)
    for i, (fx, fy, hfrac) in enumerate(pads):
        tw = int(W * 0.16 * (0.7 + hfrac))
        th = int(H * 0.028 * (0.8 + hfrac))
        cx, cy = int(W * fx), int(H * fy) - int(H * 0.018)
        d.ellipse(
            [cx - tw, cy - th, cx + tw, cy + th],
            fill=(40, 90, 55, 90),
            outline=(236, 210, 130, 220),
            width=3,
        )
        bbox = d.textbbox((0, 0), str(i), font=f)
        lw, lh = bbox[2] - bbox[0], bbox[3] - bbox[1]
        d.text((cx - lw // 2, cy - lh // 2 - 2), str(i), font=f, fill=(255, 248, 220, 255))
    out.alpha_composite(overlay)
    return out.convert("RGB")


def caption(im: Image.Image, text: str) -> Image.Image:
    out = im.convert("RGB")
    d = ImageDraw.Draw(out)
    d.rectangle([0, 0, W, 44], fill=(48, 32, 18))
    d.text((12, 10), text, font=font(22), fill=(236, 220, 180))
    return out


def grid(paths, labels, dest, title):
    cols, rows, cw, ch, header = 5, 2, 288, 512, 56
    canvas = Image.new("RGB", (cols * cw, rows * ch + header), (42, 28, 16))
    d = ImageDraw.Draw(canvas)
    d.text((16, 14), title, font=font(28), fill=(236, 220, 180))
    for i, p in enumerate(paths):
        im = Image.open(p).convert("RGB").resize((cw, ch), Image.Resampling.LANCZOS)
        x, y = (i % cols) * cw, header + (i // cols) * ch
        canvas.paste(im, (x, y))
        d.rectangle([x, y, x + cw, y + 28], fill=(48, 32, 18))
        d.text((x + 8, y + 4), labels[i], font=font(16), fill=(236, 220, 180))
    canvas.save(dest, quality=88)
    print("wrote", dest)


def debug_masks(key: str, bg: Image.Image) -> None:
    overlay = Image.new("RGBA", bg.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    colors = {2: (220, 70, 40, 110), 4: (40, 120, 220, 120)}
    for z, spec in OBJECTS[key]:
        for poly in spec.get("polys") or []:
            d.polygon(poly, fill=colors[z], outline=(255, 240, 180, 230))
        for box in spec.get("ellipses") or []:
            d.ellipse(box, fill=colors[z], outline=(255, 240, 180, 230))
    vis = Image.alpha_composite(bg.convert("RGBA"), overlay)
    vis.convert("RGB").save(DBG / f"{key}-mask.jpg", quality=85)


def compose(key: str, label: str, bg: Image.Image) -> Image.Image:
    layers = {z: Image.new("RGBA", bg.size, (0, 0, 0, 0)) for z in range(1, 6)}
    for name, fx, fy, hfrac, z in PEOPLE[key]:
        place_standee(layers[z], NPCS[name], fx, fy, hfrac)
    for z, spec in OBJECTS[key]:
        layers[z].alpha_composite(extract_object(bg, spec))
    out = bg.convert("RGBA")
    for z in range(1, 6):
        out.alpha_composite(layers[z])
    return caption(out.convert("RGB"), f"{label}  ·  2.5D")


def main() -> None:
    empty_paths, people_paths, pad_paths, labels = [], [], [], []
    for key, label in SCENES:
        bg = Image.open(ART / f"{key}.jpg").convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
        debug_masks(key, bg)
        empty = caption(bg, label)
        empty_path = OUT / f"{key}.jpg"
        empty.save(empty_path, quality=90)
        empty_paths.append(empty_path)

        people_path = OUT / f"{key}-people.jpg"
        compose(key, label, bg).save(people_path, quality=90)
        people_paths.append(people_path)

        pads = caption(draw_pads(bg, PADS[key]), f"{label}  ·  pads 0–4")
        pad_path = OUT / f"{key}-pads.jpg"
        pads.save(pad_path, quality=90)
        pad_paths.append(pad_path)
        labels.append(label)
        print("packed", key)

    grid(empty_paths, labels, OUT / "compare-sit-empty.jpg", "Market sit  ·  empty")
    grid(people_paths, labels, OUT / "compare-sit-people.jpg", "Market sit  ·  2.5D objects + different blocking")
    grid(pad_paths, labels, OUT / "compare-sit-pads.jpg", "Market sit  ·  pads")
    print("debug masks in", DBG)


if __name__ == "__main__":
    main()
