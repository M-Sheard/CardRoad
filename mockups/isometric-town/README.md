# Isometric town — LOCKED

Marc locked this as Card Road’s world display (Oct 2026).

You are a tiny cream-coat avatar. People are other walkers. Places are buildings you walk to. Match / binder / journal stay the live gilt screens.

**HUD is a separate overlay.** It is not painted into the map. `town-hud.html` sits on top of whatever scene we put underneath and resizes with the viewport (date flexes, Journal stays planted, location strip is `min(620px, 100% - 24px)`). Hardware is `hud/paper_corner.png` + `hud/paper_seal.png`. Not `date_frame_*` scrolls.

## Stills

- **HUD only:** `hud-only.jpg`
- **Game screen only:** `scene-only.jpg` (painting: `lythmere-market-scene.jpg`)
- **Together:** `lythmere-market-ingame.jpg`
- **Side by side:** `hud-and-scene.jpg`
- **Resize:** `hud-resize.jpg` (320 / 390 / 430 / 780)

Open `town-hud.html`, `town-hud.html?layer=hud`, `town-hud.html?layer=scene`.

The 01–07 stills are old concept art with HUD baked into the painting. Do not use those as the live HUD.

**Oak standees on this map:** look-test by retinting the town, not the figures. `standee-fit/` — jewel gold and warm dusk are the two that help.

Live `index.html` is untouched.

Standby (do not build): board-and-pawns, View-Master.
