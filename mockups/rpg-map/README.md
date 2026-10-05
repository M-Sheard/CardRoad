# Lythmere tabletop map (look-test)

Board-and-pawns oval/tile did not work. This is the next try: a **tabletop RPG campaign map** of Lythmere. Tap Inn, Market, Riverside, or Club and that place’s parchment plate opens.

Not a lock. Isometric town stays the current display lock until Marc picks. Live `index.html` is untouched.

## Flow

1. Phone 9:16 map (`map.jpg`) — River Wylye, the four places labelled in ink.
2. Tap a dashed box (or the cream location strip) → that location’s plate.
3. Oak-bevel cutouts stand on the plate’s yard / quay / drive.
4. **Map** returns. HUD is the cream overlay, not baked into the jpg.

Open `map.html` (phone 9:16). Overlay stills: `rpg-map-town.jpg`, `rpg-map-market.jpg`, `rpg-map-inn.jpg`, `rpg-map-riverside.jpg`, `rpg-map-club.jpg`.

Public tunnel (while this session’s server is up):

`https://walnut-activated-flashing-coupon.trycloudflare.com/mockups/rpg-map/map.html`

## Files

- `map.jpg` — campaign map
- `loc-market.jpg` `loc-inn.jpg` `loc-riverside.jpg` `loc-club.jpg` — location plates
- HUD hardware: `../isometric-town/hud/`
- Standees: `../../assets/npcs/`
