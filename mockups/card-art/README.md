# Card-face generation lock (17d tall WebP)

Live files: `assets/cards/C001.webp`–`C120.webp` (720×1280, WebP quality 80).
PNG masters: `mockups/card-art/Cxxx.png`.
Do not change C001–C120 stats.

## Painting

- Picture inside the gilt window only. No card frame, numbers, UI, caption.
- Tall 9:16 portrait. Fill the frame.
- Mary Blair mid-century storybook **gouache**, earthy/muted, visible paper texture, cartoon animal.
- Higher tier = more detail in **this same style**, not a new style.
- Animal is an animal: no cloak, staff, clothes, armor, human adventurer.
- **NO** white cottage, red roof, winding cream path, daisy-tulip kit, birch+cottage template.
- Small creatures (insects, mice, newts, chicks): subject large in the frame, readable at ~80px.

## Tiers (budget stand-in)

- common 14–16: simple shapes, few elements (Earwig C001)
- uncommon 17–19: full animal, unique habitat (Red Fox C024)
- rare 20–22: more modeled fur/feather (Sphinx C076)
- high 23–24: richer dusk/atmosphere (Chimera C089)
- top 25–26: most finish, dramatic setting (Leviathan C116)

## After each generate

1. Copy the generated PNG to `/workspace/mockups/card-art/Cxxx.png`
2. `python3 /workspace/tools/card_art_to_webp.py /workspace/mockups/card-art/Cxxx.png Cxxx`
3. Confirm `/workspace/assets/cards/Cxxx.webp` exists (~40–120 KB)
