# Lythmere — 2.5D town screen (look-test)

Designed from scratch rather than patched onto the old hex map. One layout brief,
eight art finishes, all four landmarks on screen.

Open `index.html`. The buttons under the phone swap the art and toggle the name
tags. `?art=g-safe-diorama` picks a finish straight from the URL.
`contact.html` lines all eight up side by side.

## The layout brief

Every option was generated against the same spec, which is what makes them
comparable:

- True isometric (2:1), one camera, one warm sun from the upper left so every
  shadow falls the same way.
- Four landmarks in four separate zones — **Inn** upper left, **Market** upper
  right, **Club** lower left, **Riverside** lower right — joined by dirt lanes.
- Buildings read as painted models with a contact shadow on flat ground, not as
  terrain carved out of the ground.
- No people anywhere. NPCs belong inside the location screens.
- Top ~15% and bottom ~12% kept calm (plain grass or water) so the date plaque,
  Journal button and location strip stay legible without dimming the painting.

## Options

| | finish | notes |
|---|---|---|
| **G** | diorama | lead pick — biggest readable landmarks, survives the tall-phone crop |
| **H** | flocked mat | runner-up — strongest "models sitting on a flat mat" read |
| E | close diorama | lovely, but composed too tight; clips on tall phones |
| D | flocked mat, first pass | good, landmarks smaller |
| B | toy render | |
| A | clean iso | |
| F | golden hour | warm evening mood, glowing windows |
| C | gouache | reads flat, more drawing than model |

## Why G and H hold up and the rest do not

The art is 9:16. A real phone is taller than that (390×844 is 0.46, not 0.56),
so a `cover` backdrop crops about 9% off each side. G and H were regenerated
with a deliberate band of empty grass down both edges, so nothing important is
inside the crop. The earlier options put the Market and the dock near the edge
and lose them.

## Landmark anchors

The art sits on a `.scenePlane` that keeps its own 9:16 geometry and covers
whatever shape the handset is, so anchors expressed as a percentage of the
painting stay glued to the buildings on every phone. Anchors live in the `ART`
map in `index.html`, one set per finish: `[x%, y%, width%]`.

This is a town painting, so it follows `phone-scale.mdc`: the scene is the
viewport, chrome stays planted, and there is no leftover-space board scaler —
that belongs to the card screens. Standee placement is not part of this screen;
NPCs show up in the location views via **Mark spots**.

## Checked at

`shots/fit-320x568.jpg`, `shots/fit-390x844.jpg`, `shots/fit-430x932.jpg` —
nothing clipped, no horizontal scroll, all four tags on open ground.
