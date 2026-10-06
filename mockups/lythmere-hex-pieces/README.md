# Lythmere — 3D landmarks on a flat map

Marc locked this as **every location screen** (Oct 2026). See `.cursor/rules/tabletop-locations.mdc`.

Open `index.html`. Mockup only — nothing in the live game changes.

Marc's words were that the landmarks should *"stand out from the backdrop like
there 3d models sat on a flat surface"*. The screen is two layers:

- **The flat surface** is `map-plain.jpg` — the same river valley, no hex grid.
- **The four landmarks** are keyed models composited on top.

Never generate those two layers as one picture. That is what made every
earlier pass look painted instead of tabletop.

## Recipe (repeat this)

### 1. Flat map, 9:16, no 3D, no chrome

- Canvas: **720×1280** (`9:16`). Phone crop is **390×9:16** (`#visualShell`);
  a real phone fills `100dvh`.
- Subject: empty countryside only. River, tracks, trees, hills, parchment.
- Do **not** paint buildings, people, hex grid, HUD, or the town name.
- Palette: aged sepia / olive / ochre, candlelit, vignetted. Not sunny green.
- Camera: slight downward look at a **flat** board, not a 3D valley model.

### 2. Each landmark as its own model, same camera

Generate **one building per image**, 1:1, on lime chroma `#00FF00` filling
every edge.

Shared lock for every piece:

- Camera: three-quarter, **~35° above the table**. Front wall + one side wall.
- Light: **one** warm source, **upper left**. No shadow on the green.
- Base: chunky **hexagonal** sculpted ground, visible earth **side wall**,
  pale rim along the bottom — reads as a model you could pick up.
- Palette: same as the map. Dark walnut, soot-black timber, dusty olive,
  ochre earth. Muted. Not bright, fresh, or candy.
- No people, no animals, no letters, no UI.

Then `python3 key_pieces.py chroma/piece-inn.jpg` (greenness
`g - max(r,b)`, soft 18 / full key 72). Trim, resize to **520px** wide,
keep each file under **~500KB**.

### 3. Composite in HTML, place in %

- Map is one `<img>`. Pieces sit on top with a contact shadow
  (`drop-shadow(3px 5px 5px)` + a tight ellipse under the base).
- `x` / `y` = base centre as **% of the map**. `w` ≈ **34–36%**.
  `anchor` ≈ **62–72%** down the piece image so tall models rise off the
  ground instead of sinking.
- Lower on the map = in front (`z-index` from `y`).
- Labels are HTML, not baked into the art.
- Marc drags, +/−, Copy. Do not eyeball new towns.

Baked Lythmere slots:

```
Inn       19.0  42.5  36.0  anchor 72
Club      80.1  33.7  34.0  anchor 67
Market    85.1  56.6  34.0  anchor 70
Riverside 29.7  77.6  36.0  anchor 62
```

### 4. HUD is overlay, not paint

- Date + Journal paper plaques at the top.
- Town name is HTML in the gap **under** those plaques.
- **No** bottom place-name strip on the map — the pieces are the nav.
- Safe-area insets: `max(16px, env(safe-area-inset-*) + 10px)`.

## What this recipe is for

**Yes — same method:** another town overworld, another region map, extra
landmarks (mill, quay) on this board. Same camera, same chroma, same HUD.

**Same idea, different camera:** a location *interior* (inside the Inn).
Still “flat painting + 3D things on it”, but not these 35° token pieces
and not an aerial valley. Do not reuse this prompt for a street you walk.

**No — different system:** match, binder, journal, claim, result. Those
stay leftover-space gilt / document screens.

**No — different object:** NPC standees stay Tomas bevel oak. Do not put
people on hex bases or generate new standee construction.

## Place landmarks (same as placing people)

Drag a piece. Use **+/−** or the mouse wheel to size it. **Copy** dumps the
`x y w` percentages. **Hide list** if the panel is in the way. Slots save in
`localStorage` (`cardRoadLandmarkPieces`) until you hit Reset.

This is the mockup's own placer. It is not the old street Mark spots tool, and
it is not wired into live `index.html`.

## Files

| File | Notes |
| --- | --- |
| `map-plain.jpg` | Default. Valley, no hex, no baked title. |
| `map-plain-titled.jpg` | Earlier painting with LYTHMERE in the sky. |
| `map-bare-grid.jpg` | Hex overlay, **Hex** toggle only. |
| `chroma/piece-*.jpg` | Unkeyed sources. |
| `key_pieces.py` | Lime chroma → alpha. |
