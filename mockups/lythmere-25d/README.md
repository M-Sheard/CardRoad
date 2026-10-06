# Lythmere — 2.5D town screen (look-test)

Open `index.html`. The buttons under the phone swap the scene and toggle the
name tags; `?art=concepts/v5-close-iso-square` picks one straight from the URL.
`contact.html` lines them all up side by side.

## Two passes, and why the first one missed

**First pass (A–H)** varied the *paint finish* — clean iso, toy render, gouache,
flocked mat, golden hour — across one shared **bird's-eye aerial camera**. That
was the mistake. An aerial map has no background plane, because the ground is the
entire picture, so nothing can stand *against* anything. It was also the same
composition the hex map already had, which is not "from scratch".

**Second pass (V1–V6)** varies the **camera** instead. Four of the six give you a
flat background plane with solid pieces standing in front of it.

## V1–V6

| | concept | what it is |
|---|---|---|
| **V1** | backdrop + table | Flat painted sky-and-hills board behind; four models on a flat green mat in front. Low camera, ~20°. The literal read of "3D models on a flat surface against a flat backdrop". |
| **V5** | town square | Street scale. You see fronts, doors, signs and steps. Four landmarks around one cobbled square. Reads most like a finished game screen. |
| **V2** | street level | Looking down a lane, landmarks stepping back through layers of depth to a hazy flat horizon. |
| **V4** | floating slab | One solid block of land against plain sky. The hardest separation of object from background of the six. |
| **V3** | paper theatre | Separate flat cut layers standing one behind another with visible gaps between them. Literal 2.5D in the technical sense. |
| **V6** | four pieces | Four based models against a seamless backdrop. Reads as a place picker rather than a town. |

Every one of them keeps all four landmarks — Inn, Market, Club, Riverside — in
frame, with no people on screen; NPCs belong inside the location views.

## Known rough edges

None of V1–V6 has been composed for the tall-phone crop yet. The art is 9:16 but
a phone is taller than that (390×844 is 0.46, not 0.56), so a full-bleed backdrop
loses about 9% off each side. In V1 that clips the Inn and the Market, and in V2
the dock sits uncomfortably close to the right edge. That is a one-line fix in
the prompt — a band of empty ground down both edges, as `g-safe-diorama.jpg`
already does — and it is worth doing only to whichever camera gets picked.

## Landmark anchors

The art rides a `.scenePlane` that keeps its own 9:16 geometry while covering
whatever shape the handset is, so anchors written as a percentage of the painting
stay glued to the buildings. They live in the `ART` map in `index.html`, one set
per scene: `[x%, y%, width%]`.

This is a town painting, so it follows `phone-scale.mdc`: the scene is the
viewport, chrome stays planted, and there is no leftover-space board scaler —
that belongs to the card screens. Standee placement is not part of this screen;
NPCs show up in the location views via **Mark spots**.

## Checked at

`shots/fit-320x568.jpg`, `shots/fit-390x844.jpg`, `shots/fit-430x932.jpg` for
the aerial pass, and `shots/concepts/` for V1–V6 at 390×844. No horizontal
scroll anywhere.
