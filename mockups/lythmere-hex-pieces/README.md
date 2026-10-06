# Lythmere — the signed-off hex map with raised 3D landmarks

Open `index.html`. This is a mockup only; nothing here is wired into the game yet.

## What went wrong before

Marc signed off the hex map in `../lythmere-hex-screen/05-empty-aligned.jpg`
(thin lines, hexes 35% larger, no NPCs) and asked for one change: make the four
points of interest actual 3D diorama pieces so they stand out.

Every attempt after that quietly threw the approved map away and generated a
brand new scene — bright green, sunny, and with **no hex grid at all**. The
brief was never "design a new town"; it was "same screen, landmarks raised".

## What this does instead

Marc's words were *"the landmarks should stand out from the backdrop like
there 3d models sat on a flat surface"*. So the screen is built as two layers,
not painted as one picture:

- **The flat surface** is the map, a single piece of art. No 3D in it at all.
- **The four landmarks** are separate models, each generated on its own and
  composited on top with a contact shadow.

Asking a generator for "flat map with 3D things on it" in one shot never works,
because it blends the whole frame to one depth. Splitting the layers is what
makes the pieces actually read as raised.

## The pieces

`piece-inn.png`, `piece-market.png`, `piece-club.png`, `piece-riverside.png`.

Each was generated alone on lime `#00FF00` and keyed to alpha by
`key_pieces.py` — the same chroma convention the NPC standees already use. They
share one camera (three-quarter, ~35° above), one light (upper left), one
palette, and each stands on a chunky hexagonal base with a visible side wall,
so it reads as a model you could pick up off the table.

Keyed, trimmed and resized to 520px wide, every piece is under 500KB.

```
python3 key_pieces.py /path/to/piece-inn.jpg   # writes piece-inn.png
```

## Backgrounds

Three to choose between, switchable in the dev bar:

| Map | Notes |
| --- | --- |
| `map-bare-grid.jpg` | Buildings removed, strong large hex grid. Pieces place freely. Default. |
| `map-bare-soft.jpg` | Same, but the grid is much fainter. |
| `../lythmere-hex-screen/05-empty-aligned.jpg` | The signed-off art untouched. Richer terrain and the baked serif labels, but the pieces have to sit on top of the painted buildings, and a little of the old Riverside sign and boat still peeks out. |

On the two bare maps the place names are drawn in HTML under each piece, styled
to match the serif labels inked into the original.

Stills of the look-test live in `shots/` (`clean.jpg` without HUD, `phone.jpg`
with the paper chrome, `board-only.jpg` with the pieces hidden). Chroma
sources for re-keying are in `chroma/`.

## Placement

`PIECES` in `index.html` holds `x` / `y` — where the model's base centre lands
on the map — plus `w` and `anchor`, how far down its own image that base centre
sits. `anchor` is what stops a tall model sinking into the ground. The dev bar
scales all four together for sizing.

## Still open

The baked `LYTHMERE` title sits behind the date plaque. Either drop the title
from the art or move the plaque down before this goes near the game.
