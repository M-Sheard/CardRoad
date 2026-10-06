# Lythmere — 3D landmarks on a flat map

Open `index.html`. Mockup only — nothing in the live game changes.

Marc's words were that the landmarks should *"stand out from the backdrop like
there 3d models sat on a flat surface"*. The screen is two layers:

- **The flat surface** is `map-plain.jpg` — the same river valley, no hex grid.
- **The four landmarks** are keyed models composited on top.

## Place landmarks (same as placing people)

Drag a piece. Use **+/−** or the mouse wheel to size it. **Copy** dumps the
`x y w` percentages. **Hide list** if the panel is in the way. Slots save in
`localStorage` (`cardRoadLandmarkPieces`) until you hit Reset.

This is the mockup's own placer. It is not the old street Mark spots tool, and
it is not wired into live `index.html`.

## Pieces

`piece-inn.png`, `piece-market.png`, `piece-club.png`, `piece-riverside.png`.

Each was generated on lime `#00FF00` and keyed by `key_pieces.py`. They share
one camera, one light, and a chunky hexagonal *base* so they still read as
models you could pick up. The hex *grid* on the map is gone.

## Maps

| File | Notes |
| --- | --- |
| `map-plain.jpg` | Default. Same valley, hex lines removed. |
| `map-bare-grid.jpg` | The hex overlay, still there behind the **Hex** toggle if you want it back. |

`x` / `y` are where the model's base centre lands, as a % of the painting.
`anchor` is how far down its own image that base sits, so a tall model rises
off the map instead of sinking into it.
