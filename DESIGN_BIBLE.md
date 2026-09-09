# CARD ROAD

## Definitive Game Design Bible

**Document status:** Living canonical design bible  
**Current development state:** Core gameplay validated through playable prototype (PWA v21 — UI Geometry Fix)  
**Production distribution (locked intent):** iOS App Store, Google Play, and Steam, all shipping the **same web core** (not a Unity/Godot rewrite)  
**Purpose:** Preserve the agreed vision, mechanics, world principles, progression systems, UI direction, testing conclusions, deferred concepts, numerical roster, and unresolved design questions for continued development.

### Source artefacts

| Artefact | Role |
| --- | --- |
| This document | Vision, systems, production priorities, and operator constraints |
| `Card_Road_Definitive_Numerical_Roster_and_Handover.docx` | Authoritative Baseline V1 numerical roster (C001–C120) |
| `CardRoad_PWA_v21_UIGeometryFix.zip` | Current playable implementation; UI geometry pass only |
| Older 1–5 mock-up values | Historical only — **not** current roster |

Older prototype/mock-up card values, including many 1–5 examples, must not be used as the current roster.

---

# 1. HIGH-LEVEL CONCEPT

Card Road is a persistent-world, single-player card game built around a simple and highly readable **3×3 positional card battle system**.

Its core inspiration comes from the immediacy and strategic clarity of games such as Triple Triad, but Card Road is intended to become substantially more than a sequence of isolated card matches.

The central concept is:

> **A card game that exists inside a living world.**

Cards are physical objects within that world.

NPCs own cards.

NPCs play one another.

Cards change hands.

Players remember one another.

Individual copies develop histories.

Tournaments create champions.

Prestigious cards circulate through the community.

News spreads about important events.

The player gradually moves from being an unknown local player into a participant in a much larger competitive card culture.

The game should remain easy to understand while allowing considerable emergent depth to develop from the interaction between simple systems.

---

# 2. CORE DESIGN PHILOSOPHY

Card Road should prioritise:

- Simple rules with meaningful consequences.
- Fast, enjoyable individual matches.
- Persistent consequences between matches.
- Genuine ownership of cards.
- A world that continues beyond the player.
- NPCs who feel like people rather than opponent menus.
- Cards that can develop individual histories.
- Tournaments that feel important.
- Collecting without turning cards into disposable upgrade materials.
- Strategic variety without excessive rule complexity.
- Strong visual identity.
- Long-term discovery.
- Player freedom rather than mobile-game-style task lists.

The game should **not** become overloaded merely because another mechanic could be added.

New mechanics should answer:

> **Does this make the existing game more interesting?**

Complexity must justify itself.

---

# 3. CORE GAMEPLAY LOOP

The fundamental loop is:

**Explore the card-playing world**

↓

**Meet and develop relationships with players**

↓

**Challenge or receive challenges from NPCs**

↓

**Negotiate/select match rules**

↓

**Build/select a hand**

↓

**Play a 3×3 card match**

↓

**Cards may change ownership**

↓

**NPC relationships and memories develop**

↓

**The wider card economy continues operating**

↓

**News reports significant events**

↓

**Calendar advances**

↓

**Scheduled competitions and tournaments occur**

↓

**Results permanently affect cards, characters and the world**

↓

**Progress toward increasingly prestigious competitive environments**

The player should eventually feel that an apparently simple card match exists inside a much larger network of consequences.

---

# 4. MATCH FOUNDATION

## 4.1 Board

Matches take place on a **3 × 3 grid**. There are nine playable positions.

Cards possess numerical values on their four sides:

- Top (North)
- Right (East)
- Bottom (South)
- Left (West)

When opposing cards become adjacent, the appropriate facing values are compared according to the active rules.

Control of cards can change during play.

The exact tested match engine currently provides the mechanical foundation and should not be casually altered now that playtesting has established that matches are enjoyable.

## 4.2 Established match UX (do not regress)

The existing match layout has undergone extensive usability testing. Preserve:

- Board fits cleanly without clipping.
- Player cards must not overlap the board.
- NPC cards must not overlap the board.
- Thinking indicators must not move core board geometry.
- Duplicate selection must be unambiguous.
- When an NPC places the **final card**, the player must see that card and the completed board before the result screen.
- Claim interface must remain accessible.
- Match flow should remain smooth.

Do not skip from NPC thinking straight to Victory/Defeat.

---

# 5. CARD DESIGN

## 5.1 Fixed statistics

Cards have fixed numerical statistics.

Cards do **not** level up.

The game deliberately avoids:

- a card XP system;
- a stat-upgrade system;
- duplicate fusion;
- duplicate-based power progression.

A Riverling remains a Riverling.

Its value comes from usefulness, scarcity, ownership history, tournament history, provenance, collector interest, and personal meaning.

## 5.2 Definitive numerical baseline (V1)

This is the **authoritative transfer reference** for Card Road’s current numerical card system.

| Rule | Canon |
| --- | --- |
| Profile IDs | 120 fixed IDs, **C001–C120** |
| Sides | Four fixed values: North, East, South, West |
| Side range | Integer **1–10** |
| Card total | N + E + S + W |
| Total range | Every integer total **14–26** is represented |
| Orientation | Part of identity. Rotating or reassigning the same four numbers creates a different tactical profile |
| Deck cost (current) | Total currently also acts as deck-budget cost |
| Names | Placeholder only (`Design 001`, etc.). Not final identities |
| Rarity | **Separate** from numerical strength |

**Operator must preserve**

- All 120 C001–C120 profiles and their exact N / E / S / W orientation.
- Side values 1–10 and totals 14–26.
- Geometry mix: Balanced, Adjacent Pair, Opposite Pair, Single-Side Specialist, Asymmetric, Extreme Specialist.
- Separation between numerical strength and rarity/circulation scarcity.
- Current budget-test formats: **82 low**, **86 primary candidate**, **92 high**, plus unrestricted as a separate format.
- Version discipline: numerical changes create a later baseline (e.g. V2). Do not silently mutate Baseline V1.

**Operator must not assume**

- That old 1–5 mock-up values are current.
- That a high-total card must be rare, or a low-total card must be common.
- That placeholder names are final card identities.
- That every profile is permanently balanced merely because it appears in V1.
- That a stale spreadsheet Summary tab is authoritative. **Roster V1** is the source of truth.

### Deck-budget model

A five-card deck costs the sum of the five cards’ totals. Example: C001 is 3 / 5 / 3 / 3 = **14**.

Budget formats 82 / 86 / 92 are **balance candidates**, not immutable final canon. Deck budget is accepted for **some competitions**, not as a universal rule.

If deck cost remains identical to Total, prefer a field name such as `deckCost` rather than overloading “budget”.

### Geometry and tactical identity

Equal-total cards are deliberately **not** equivalent. Example: C076 (6/6/5/5, total 22) is balanced; C081 (10/10/1/1, total 22) is an extreme specialist. Both cost 22 but behave very differently on a 3×3 board.

| Geometry | Tactical purpose |
| --- | --- |
| Balanced | Strength spread relatively evenly across four sides |
| Adjacent Pair | Two neighbouring sides carry the main strength |
| Opposite Pair | Two opposing sides carry the main strength |
| Single-Side Specialist | One side substantially stronger than the rest |
| Asymmetric | Uneven profile that does not fit a cleaner specialist shape |
| Extreme Specialist | Very high values (often 9 or 10) paid for with very weak sides |

### Verified roster distribution (recalculated from Roster V1)

**By total**

| Total | Count | Total | Count |
| --- | --- | --- | --- |
| 14 | 6 | 21 | 12 |
| 15 | 7 | 22 | 11 |
| 16 | 8 | 23 | 10 |
| 17 | 9 | 24 | 9 |
| 18 | 10 | 25 | 8 |
| 19 | 11 | 26 | 7 |
| 20 | 12 | **Sum** | **120** |

**By geometry:** Adjacent Pair 33 · Opposite Pair 23 · Balanced 21 · Single-Side Specialist 19 · Extreme Specialist 13 · Asymmetric 11

**By working role:** Core 35 · Flexible support 30 · Economy / specialist 21 · Premium 19 · Marquee 15

### Confirmed vs not finalised

**Confirmed working baseline:** 120 IDs; four directional values; sides 1–10; totals 14–26; exact Appendix A profiles; geometry labels and working roles; total currently functions as deck cost; 82 / 86 / 92 as implemented budget-test formats; numerical strength separate from rarity/circulation.

**Not finalised by this baseline:** final names, creature identities, art, lore, families, flavour; final rarity and circulation of each profile; whether 86 remains the permanent main competitive budget; whether every individual profile survives unchanged after extensive balance testing.

### Recommended data schema

```json
{
  "id": "C001",
  "north": 3,
  "east": 5,
  "south": 3,
  "west": 3,
  "total": 14,
  "deckCost": 14,
  "geometry": "Balanced",
  "role": "Economy / specialist",
  "numericalBaseline": "V1"
}
```

Attach future name/art/lore metadata to the stable numerical ID. Do not replace the ID. Do not regenerate the entire roster for implementation convenience. Test suspected outliers in actual matches and deck-building before changing values.

The full C001–C120 table is **Appendix A**.

---

# 6. PHYSICAL CARD OWNERSHIP

Cards should be treated as individual physical objects rather than merely database unlocks.

If the player owns two copies of the same card, those are **two separate copies of that card**.

This becomes particularly important once provenance develops.

Two mechanically identical copies could eventually have completely different histories.

**Riverling — Copy A:** ordinary circulation, no tournament history.

**Riverling — Copy B:** previously owned by Tomas, won by the player, later used to win a championship.

Mechanically identical. Historically different.

---

# 7. GENUINE CARD LOSS

Card loss is real.

If match rules allow the opponent to claim a card and the player loses, **the player actually loses ownership of that card**. The card enters the winner’s collection.

Do not secretly duplicate or restore cards merely to protect the player from consequences.

---

# 8. DUPLICATES

Duplicates are legitimate physical copies.

Common cards can exist in significant numbers throughout the world.

Duplicates are **not** consumed to increase card statistics.

Potential uses: trading, exchange systems, collection decisions, entry mechanisms where appropriate, exchanging multiple cards for another card.

The exact long-term exchange economy remains subject to balancing.

---

# 9. CARD SCARCITY

Common cards can circulate freely and exist in effectively unrestricted quantities where appropriate.

Higher-rarity cards should have increasingly controlled circulation.

Scarcity should make discovering and following particular cards interesting.

At the extreme end are prestige cards.

---

# 10. PRESTIGE CARDS

Prestige cards are exceptionally scarce status objects.

> **Prestige must not equal superior competitive power.**

A World Championship prestige card can have the same effective power level as another top-tier card.

Its value comes from extreme scarcity, achievement, provenance, artwork, history, and recognition.

This prevents championship winners from receiving cards that simply make them even harder to defeat.

---

# 11. ALTERNATE ARTWORK

A future possibility is for important competitions—particularly World Championships—to award an alternate artistic edition of an existing card.

The standard version and World Championship version are mechanically identical. The championship version might feature unique artwork, special border treatment, commemorative presentation, and provenance connected to the competition.

Strongly liked; introduce carefully rather than flooding the initial game with variants. Alternate artwork should feel prestigious rather than becoming conventional skin spam.

---

# 12. CARD PROVENANCE

Individual card copies can accumulate history: previous owners, notable transfers, tournament victories, championship history, important competitive moments.

Provenance creates the possibility that an otherwise ordinary card becomes culturally important because of what happened to that specific copy.

---

# 13. TOURNAMENT STAMPS

**Cards are stamped only when they win a tournament.** Ordinary match victories do not create stamps.

This prevents provenance from becoming cluttered. A heavily travelled card may have an extensive ownership history but only a small number of prestigious tournament stamps.

---

# 14. CARD FAMILIES

Cards may belong to thematic families.

Families primarily provide lore, artistic cohesion, world-building, and collector identity.

Card families do **not** automatically grant gameplay bonuses merely for belonging to the same family.

---

# 15. COLLECTION KNOWLEDGE

NPC collections are not automatically completely visible.

Knowledge should distinguish between:

- **Owned** — the player currently owns the card.
- **Seen** — the player has encountered or learned about the card.
- **Unknown** — the player has not discovered the card.

Unknown cards should remain genuinely unknown rather than having their information conveniently exposed.

---

# 16. CARD-SELECTION UI

When multiple copies of the same card exist, selection must clearly communicate which physical copy is selected.

Highlighting every duplicate identically when only one copy had actually been selected was confusing.

The interface must distinguish: selected copy; other owned duplicates; unavailable/non-selectable copies.

At a glance, the player should always know exactly how many cards are selected.

---

# 17. CARD CLAIM UI

When winning a card-selection match, the player should be able to see available cards, whether each card is already owned, and number of copies currently owned.

---

# 18. NPC CARD ECONOMY

NPCs genuinely own collections. NPCs can play one another. Cards can transfer between NPCs without player involvement.

The player is **not the centre of the card economy**.

A card lost to Tomas might later be lost by Tomas to another player, enter a tournament, move again, and eventually become available to the player again.

---

# 19. LOCAL CARD ECONOMY DEBUGGING

Internal economy information is useful for testing.

> **The Local Card Economy panel is a developer/testing feature and should be hidden from the normal player-facing game.**

Development interfaces should be labelled **TEST / DEBUG** and be removable or hidden in production.

The player should discover the world through appropriate in-world information rather than omniscient simulation data.

---

# 20. CARD NEWS

Card News communicates significant activity in the wider card community: notable transfers, tournament results, championship victories, unusual circulation events, important competitive developments.

It should help create the impression that the card world exists independently of the player. It should not become a raw debug log.

---

# 21. CHALLENGE SYSTEM

Challenges work in both directions. The player can challenge NPCs. NPCs can challenge the player. NPCs should possess apparent agency.

---

# 22. CHALLENGE AUTHORITY

The **challenged party** determines the proposed rules.

The challenger then chooses whether to accept or decline.

This applies regardless of whether the player or NPC initiated the challenge.

---

# 23. MATCH SERIES

Supported structures include single match, Best-of-3, and Best-of-5.

Different contexts can legitimately use different structures. This is particularly useful for tournament and ranked formats.

---

# 24. TOURNAMENT FORMAT

Current tournament testing established a format that feels good.

- Standard tournament rounds: **Best-of-3**
- Tournament final: **Best-of-5**

This increases tension and makes finals feel more significant.

---

# 25. TOURNAMENT DRAWS

Tournament matches cannot end in unresolved draws. Tournament structure must always produce a player who advances.

The tournament must remain completable if the player loses before the final. Player elimination must never strand the tournament state. The tournament continues and resolves without requiring the player to remain involved.

---

# 26. FINAL NPC MOVE

When an NPC places the final card in a match, the player must be allowed to see that card and the completed board before the result screen appears.

Never skip directly from **NPC thinking** to **Victory/Defeat** without showing the decisive move.

---

# 27. TOURNAMENT RULE VARIETY

Different tournaments may legitimately use different rule configurations. Rules can help tournaments develop identities without requiring every possible rule to appear simultaneously.

---

# 28. RULE EXPLANATION

Every selectable rule should have a brief tooltip or equivalent explanation.

Before a match begins, the player should see a clear summary of the **complete active ruleset**.

The player should never enter a match without understanding what rules are active.

---

# 29. RULE COMPLEXITY PRINCIPLE

Not every successful experimental rule belongs in the starter game.

Some tested mechanics were deliberately retained as possibilities for later patches, expansions, or special competitions.

This protects the initial experience from unnecessary complexity.

Prototype currently exposes experimental toggles for reverse capture, hand visibility, and combo chains. These are **TEST / DEBUG** comparison controls, not permanent starter-game rules.

---

# 30. DECK BUDGET SYSTEM

A deck-budget system has been accepted for use in **some competitions**. It is not a universal rule.

Different tournament/ranked formats can use different deck-building restrictions.

Working test thresholds in the current build: **82 / 86 / 92**, with **86** as the primary candidate and unrestricted as a separate format. Exact production thresholds require later balancing.

---

# 31. ANTI-FARMING

The world uses time and event structure to prevent players repeatedly farming valuable weekly/periodic competitions without consequence.

The production implementation should respect the world calendar rather than feeling like an arbitrary mobile-game cooldown.

---

# 32. CALENDAR

## Important canonical correction

The earlier 30-day prototype season structure is **not the final calendar**.

The agreed production design uses **a 365-day in-world calendar**.

The 30-day implementation was prototype/testing compression and has now been superseded as a world-design assumption.

Future tournaments, events, NPC schedules, world simulation, progression, championships, travel, and seasonal activity must be designed around the **365-day calendar**.

Do not reintroduce the 30-day season as production canon unless deliberately reconsidered.

The v21 prototype already generates a year of events (weekly Saturday locals, seasonal fairs). That direction is consistent with this canon.

---

# 33. TIME AS AN ANTI-FARMING SYSTEM

The calendar should naturally limit opportunities.

If a championship occurs once per year, the player cannot simply replay it repeatedly.

Time therefore gives competitions scarcity, anticipation, consequence, and prestige. This is preferable to arbitrary energy systems.

---

# 34. INTRODUCTION / TUTORIAL

The opening sequence begins with the player’s grandfather.

The player and grandfather each have **five pre-selected cards**.

The tutorial introduces the fundamental match system.

After the opening match, the player receives:

- both sets involved in the tutorial;
- approximately five additional random cards.

The player is then directed toward the first mentor/NPC/location and begins entering the wider card-playing community.

---

# 35. PLAYER REPUTATION

Reputation is **hidden and multidimensional**. There is no simple visible reputation meter.

The player infers reputation through NPC reactions, invitations, challenge behaviour, tournament access, social opportunities, Card News, recognition, and competitive standing.

---

# 36. RANKING VS REPUTATION

Competitive ranking and reputation are related but distinct.

A player can be highly ranked but disliked; respected despite modest ranking; famous for unusual cards; known for risky wagers; recognised for championship performance.

World/regional ranking influences reputation but does not define it.

---

# 37. NPC RELATIONSHIPS

Relationships are not simply rivalry meters.

The game supports friendship, rivalry, friendly rivalry, warm acquaintance, competitive acquaintance, and strained/cold relationships.

Friendship and rivalry are **separate underlying dimensions**.

> Someone can genuinely like the player while desperately wanting to beat them.

This allows **Friendly Rival** relationships.

---

# 38. RELATIONSHIP PRESENTATION

Raw numerical relationship values remain hidden.

Players instead observe relationships through qualitative descriptions, dialogue/reactions, challenge frequency, willingness to accept rules, rematch behaviour, remembered history, and card-related behaviour.

---

# 39. NPC MEMORY

Permanent NPCs can remember meaningful interactions such as matches, series, victories, defeats, cards won, cards lost, declined challenges, and significant competitive moments.

Profiles can show remembered moments without exposing the underlying simulation numbers.

---

# 40. FRIENDSHIP

Repeated positive interaction can create genuine friendship.

Friends may seek games simply because they enjoy playing the player; trust the player more when negotiating match terms; respond differently to wins and losses.

Friendship should not automatically become a gameplay reward dispenser.

---

# 41. RIVALRY

Competitive history can produce rivalry: repeated close matches, important victories, card exchanges, rematches, tournament encounters.

A rival should feel competitively invested in the player.

---

# 42. FRIENDLY RIVALRY

Friendly Rival requires both genuine warmth and substantial competitive history.

It should develop through repeated meaningful interaction rather than appearing after a handful of matches.

---

# 43. NPC PERSONALITY

Prototype personalities currently establish the intended principle. These are **not yet final biographies**.

| Design-bible personality | Intended behaviour | Current v21 implementation name |
| --- | --- | --- |
| **Tomas** | Hot-blooded, risk tolerant, highly competitive. Strongest natural rivalry tendency. | Tomas |
| **Mara** | Respectful and comparatively balanced between warmth and competitiveness. | Implemented as **Bram** |
| **Nessa** | Warm and friendly. More naturally inclined toward friendship than rivalry. | Nessa |
| **Orin** | Reserved and competitive. Relationships develop more slowly. | Implemented as **Elira** |

**Open naming decision:** whether production uses Mara/Orin (design bible) or Bram/Elira (current playable art and code). Do not silently treat either pair as locked until this is resolved.

---

# 44. RELATIONSHIP PACING

Updating relationships after every game in a Best-of-3/5 caused relationships to progress far too quickly.

> **Relationship development occurs once per completed match/series, not once per individual game within a series.**

This prevents tournament play from artificially accelerating social relationships.

---

# 45. TEMPORARY NPCs

Temporary tournament visitors should not automatically develop permanent social relationship records.

Permanent relationships are primarily for characters who actually exist within the persistent social world.

---

# 46. NPC BEHAVIOUR AND RELATIONSHIPS

Relationships should influence behaviour rather than merely change profile text.

Examples already explored: friends more willing to accept unusual match terms; friendly rivals seeking another close contest; rivals wanting decisive longer series; NPCs seeking rematches; NPCs trying to recover cards previously lost; repeated declined challenges cooling relationships.

Continue moving toward behavioural consequences rather than excessive dialogue.

---

# 47. WORLD STRUCTURE

The current prototype is intentionally tiny.

The production game should eventually contain a broader card-playing world.

Development should **not** immediately generate a huge number of shallow locations and NPCs.

> Build one convincing starting location first.

---

# 48. STARTING LOCATION

The initial region should function as a real community.

Potential functional locations: player/home area; tavern or card-playing gathering place; tournament venue; Card News/notice location; collection access; map/travel access; local players.

Existing prototype NPCs can become actual residents rather than names in a menu.

### Prototype starting town (implementation, not fully locked lore)

The v21 PWA presents **Lythmere**:

| Location | Current presentation |
| --- | --- |
| Market | Lythmere Market — stalls, gossip, ordinary games beside the river |
| Riverside | Lythmere Riverside — quieter quay; travellers and locals |
| Inn | Gathering place |
| Card Club | Organised card scene and weekend tournament venue |

Starting-town identity is listed as an open design question. Lythmere is the strongest current candidate because it already has art, NPC placement, noticeboard, and Saturday opens.

---

# 49. THE WORLD SHOULD CHANGE VISIBLY

Calendar events should affect locations.

Before a major championship: banners appear; visitors arrive; NPC behaviour changes; Card News discusses preparations; competitors practise; tournament spaces become active.

Afterward: the champion is recognised; winning cards gain provenance; visitors leave; news reports the result; the world remembers what happened.

This transforms calendar events from menu entries into world events.

---

# 50. COMPETITIVE PYRAMID

**Local competition → Regional circuit → Higher national/continental competition → World Championship**

Exact tiers and geography remain to be fully designed.

Reaching the World Championship should feel like an enormous achievement rather than simply clicking the next tournament.

---

# 51. WORLD CHAMPIONSHIP

The World Championship represents the top of the competitive culture.

Potential rewards: recognition; permanent historical record; extremely prestigious tournament provenance; championship stamps; rare prestige/commemorative artwork.

It should not simply award an overpowered card.

---

# 52. ART-DIRECTION DEVELOPMENT

Visual development has begun but is **not yet completely locked**.

The strongest current direction:

## The Illustrated Card World

Warm; hand-painted; whimsical; inviting; richly illustrated fantasy environments; readable game UI; cards visually belonging to the same world.

Card-face creature paintings (the picture inside the gilt window, not the frame itself) are locked as **17d earthy Mary Blair gouache**. Canonical example: `mockups/card-art-dir-17d-blair-earthy-red-fox.png`. NPC standees remain a separate lock (Tomas bevel v19).

---

# 53. VISUAL DIRECTIONS EXPLORED

1. **The Illustrated Card World** — warm, hand-painted, whimsical fantasy. Strongest candidate.
2. **Living Medieval Manuscript** — illuminated manuscript / historical chronicle. Strong for provenance and records.
3. **Fantasy Graphic Novel** — bold characters, dramatic compositions, clean UI. Strong for NPC personality.
4. **Fantasy Travel Journal** — sketchbook, maps, annotations. Strong for travel and provenance.
5. **Living Watercolour** — dreamlike painterly environments. Beautiful; potentially harder for UI readability.
6. **Pop-Up Fantasy World** — physical diorama. Strong for a changing world; technically demanding.
7. **Stained-Glass Fantasy** — luminous, iconic. Especially promising for prestige/commemorative cards.
8. **Woodcut / Printmaker Fantasy** — carved textures, historical print language. Could support regional editions.

---

# 54. POSSIBLE HYBRID VISUAL IDENTITY

**The Illustrated World:** storybook/illustrated environments + graphic-novel-quality character portraits + travel-journal / printed-card interface.

This would keep the world warm, colourful, welcoming, and fantastical, while giving the interface a distinctive Card Road identity.

---

# 55. REGIONAL ART TRADITIONS

Promising future concept: different regions possess their own artistic traditions.

Examples: heavier inks in the north; luminous watercolour on the coast; illuminated manuscripts for ancient cards; woodcut printing in another culture.

This could justify alternate artwork **inside the fiction** as regional editions, historical printings, commemorative printings, and championship editions — rather than arbitrary cosmetic skins.

Under consideration; not locked production canon.

---

# 56. UI PHILOSOPHY

The current prototype interface is a development interface. It proves systems but contributes heavily to the game’s current barebones feeling.

Production UI should move away from a collection of functional HTML panels.

The interface should help create the illusion that the player occupies a real card-playing world.

---

# 56A. DISTRIBUTION AND CLIENT PLATFORM

Card Road is developed as a **self-contained web game** (currently a portrait PWA). That client is the production core.

**Locked shipping targets**

- **Phones:** Apple App Store (iOS) and Google Play (Android).
- **Desktop:** Steam.
- **Same game:** one web codebase; native or desktop **shells wrap it**. Do not rebuild the match, world, or roster in Unity, Unreal, or Godot in order to reach stores.

**How each store is reached (later, not during the Lythmere prototype)**

| Store | Intended path |
| --- | --- |
| Google Play | Native wrapper (e.g. Capacitor) or Trusted Web Activity |
| Apple App Store | Native wrapper (e.g. Capacitor → iOS). A “open this website” PWA is not an App Store product. The build must play fully offline, look like a standalone app, and include no TEST/DEBUG player surface |
| Steam | Desktop shell (e.g. Tauri or Electron) loading the local web build |

**Operator constraints**

- Core play must keep working **offline from local files**. Do not make the loop depend on a live server.
- Do not add Capacitor, Xcode, Steamworks, accounts, or cloud saves until Lythmere plays well and saves persist.
- Steam will need a **desktop layout** in addition to the current portrait phone layout (letterbox or a wider town/match view). That is a UI job on the same web core.
- App Store submission must feel like an installed app, not a Safari bookmark.
- Replacing `localStorage` with a desktop-safe save file is a later **structure change** and must be called out before it is done.

This is a distribution decision. It does not change match rules, Baseline V1 numbers, or the “presentation + world first” priority.

---

# 57. LOCATION-BASED UI

A promising production direction is a location/home interface.

Instead of merely selecting menu panels, the player sees where they currently are.

Natural routes can lead toward players, collection, Card News, tournaments, rankings, map, journal/history.

v21 already takes a step in this direction (town scene, location strip, journal overlay) while still exposing many debug panels on the home screen.

---

# 58. MATCH UI

Treat the current functional layout as a **usability baseline** when redesigning visuals.

Do not sacrifice tested usability merely to make the match screen prettier.

See §4.2.

---

# 59. CARD INSPECTION

Card inspection should eventually become one of the most satisfying interfaces in the game.

A card view could communicate: artwork; directional values; family; edition; ownership; provenance; previous owners; tournament stamps; historical significance.

The physical copy should feel like an object worth inspecting.

---

# 60. COLLECTION PRESENTATION

The collection should eventually feel closer to an actual card collection than a database list.

The Travel Journal / illustrated-album direction is particularly promising.

As the player progresses, their collection interface itself could become a visual record of their journey.

---

# 61. TOURNAMENT PRESENTATION

Tournaments should feel dramatically different from ordinary matches.

Presentation can communicate tournament identity, bracket, current stage, opponent, stakes, tournament rules, previous results, and final status.

Finals deserve increased presentation weight because they use Best-of-5 and represent the culmination of the event.

---

# 62. DEBUG VS PLAYER INFORMATION

Useful simulation information can remain visible during testing.

Developer-only information must be clearly labelled and removable from the final player interface.

Examples: local card economy internals; simulation state; raw relationship numbers; hidden reputation calculations; AI reasoning information.

The player should experience consequences, not omniscience.

---

# 63. WHAT TESTING HAS PROVEN

# THE GAME IS FUN.

This has been explicitly confirmed through actual play rather than assumed from the design.

Successful elements include: core 3×3 matches; card-selection decisions; tournament structure; Best-of-3 tournament rounds; Best-of-5 finals; wagering/card-loss tension; smooth match flow; persistent card ownership.

This is a major development milestone.

---

# 64. CURRENT PROBLEM: BAREBONES FEELING

Although the game is enjoyable, the prototype currently feels barebones.

This is **not primarily a core-gameplay problem**.

The major missing layers are now: production-quality UI; world presentation; location identity; character identity; art; environmental context; broader progression; world population.

The next development phase should focus more heavily on **PRESENTATION + WORLD** rather than continuing to stack mechanical systems.

---

# 65. FEATURES NOT TO RUSH INTO THE STARTER GAME

Do not currently add merely for additional complexity:

- crafting;
- conventional shops without a demonstrated need;
- large quest systems;
- card abilities;
- huge NPC cast;
- excessive match modifiers;
- duplicate upgrading;
- card levelling;
- visible relationship meters;
- visible reputation meters.

Some may eventually have a place. None currently justify destabilising the proven core.

---

# 66. DEFERRED EXPANSION CONCEPTS

Worth preserving for later: alternate championship artwork; regional card editions; additional match/tournament rule variants; deeper regional competition; world-level championships; broader travelling card economy; additional social consequences; more sophisticated provenance; special tournament formats.

Deferred does not mean rejected.

**Do not overload the starter experience before the core world is fully established.**

---

# 67. OPEN DESIGN QUESTIONS

### Card economy

- Exact rarity distribution.
- Exact duplicate exchange rates.
- Exact controlled-circulation mechanisms.

### Tournament economy

- Exact prize structures.
- Exact deck-budget thresholds (86 remains a candidate, not locked).
- Whether some tournaments require card contributions for entry.
- Additional tournament formats.

### Match series

- Exact use of tie-break wager rules outside tournaments.
- Which series formats belong to which competition types.

### World

- Starting town identity (Lythmere is implemented; not fully locked).
- Starting region.
- Wider geography.
- Number and structure of competitive regions.
- Travel mechanics.

### NPCs

- Final biographies.
- Final names for the Mara/Bram and Orin/Elira pair.
- Larger local population.
- Long-term relationship consequences.
- Social opportunities beyond challenges.

### Cards

- Final roster identities (names, creatures, families).
- Final numerical balance after more testing (Baseline V1 is the current freeze).
- Final rarity structure.
- Final family lore.
- Final artwork system.

### Visual identity

- Whether Illustrated Card World becomes the final foundation.
- Which elements of manuscript, graphic novel and travel journal presentation should be incorporated.

---

# 68. PRODUCTION PRIORITIES

## Phase 1 — Visual identity

Resolve the production art direction.

Develop representative screens for: starting town/home; normal match; card collection; tournament; NPC interaction/profile.

## Phase 2 — Starting world

Build one convincing starting community.

Establish: location; residents; card culture; tournament venue; local competitive hierarchy; visible calendar activity.

## Phase 3 — Production UI

Replace prototype panels with the real navigation and visual language.

Preserve tested match usability.

Hide TEST/DEBUG surfaces from the player-facing game.

## Phase 4 — World integration

Connect: NPC schedules; Card News; tournaments; relationships; card circulation; calendar; visible environmental change.

## Phase 5 — Expanded progression

Only once the starting area works convincingly: additional locations; regional circuit; larger NPC population; higher tournament tiers.

## Phase 6 — Championship endgame

Develop the route toward the World Championship and prestige ecosystem.

## Phase 7 — Store shells

Only after the web game feels like a finished local app:

- Hide all player-facing debug.
- Confirm full offline play.
- Add a desktop layout for Steam.
- Wrap the same build for iOS, Android, and Steam.
- Do not start this phase by changing game engines.

---

# 69. CORE EXPERIENCE TARGET

A successful Card Road session should produce stories without requiring scripted quests.

Examples:

> “Tomas won my favourite card from me, then lost it to Mara two weeks later. I finally got it back by beating Mara in the regional qualifier.”

> “That Riverling isn’t rare, but it’s the copy I used when I won my first championship. It has three tournament stamps now.”

> “Nessa started as an easy opponent. Years later she’s one of my closest friends and still keeps beating me in finals.”

> “I saw that card when I first arrived in town but couldn’t win it. Months later it appeared in Card News because someone took it to another region.”

Those stories emerge from systems interacting. That is the heart of Card Road.

---

# 70. DESIGN NORTH STAR

Card Road should ultimately feel like:

> **A simple card game embedded inside a living competitive culture where people, places and individual cards develop histories over time.**

The 3×3 match is the foundation. It is not the entire game.

The world around the match is what should make Card Road distinctive.

---

# 71. CURRENT CANON SUMMARY

Treat as foundational unless deliberately revisited:

- 3×3 positional card battles.
- Four directional card values (N/E/S/W), integers 1–10, totals 14–26.
- 120 fixed Baseline V1 profiles C001–C120; orientation is identity.
- Total currently equals deck cost; 82 / 86 / 92 are test formats, not locked forever.
- Fixed card statistics. No card levelling. No duplicate stat upgrades.
- Persistent physical card ownership. Genuine card loss. Duplicates are separate copies.
- NPC-to-NPC matches and world card circulation.
- Card News. Seen / Owned / Unknown information.
- Hidden multidimensional reputation.
- Two-way challenges. Challenged party sets rules.
- Multiple match-series formats.
- Tournament draws must resolve. Best-of-3 rounds. Best-of-5 finals. Elimination cannot block progression.
- Some competitions can use deck budgets.
- Rule explanations/tooltips. Full rules summary before matches.
- Tournament-only provenance stamps.
- Hidden two-dimensional friendship/rivalry. Friendly rivalry. NPC memory.
- Relationship changes once per completed match/series.
- Temporary visitors excluded from permanent relationships.
- Prestige cards based on status rather than superior power.
- 365-day in-world production calendar.
- Grandfather opening/tutorial.
- Starting local community before large-scale world expansion.
- Production UI should become location/world based.
- Debug information must remain separate from player information.
- Ship targets: **iOS App Store, Google Play, and Steam**, wrapping one **offline web core**. Not an engine rewrite.
- Store wrappers, desktop layout, and native save files are deferred until the web game is worth wrapping.
- Current core gameplay has been validated as fun.
- Immediate development emphasis: **art direction, production UI and world-building**.
- Do not mutate Baseline V1 in place; version as V2 if numbers change.

---

# 72. PROJECT STATUS

Card Road has moved beyond the stage of asking:

> “Can this concept work?”

The playable prototype has demonstrated that it can.

The current development question is:

> **How do we turn this enjoyable prototype into a world players want to inhabit?**

The next major leap should therefore come from **identity rather than complexity**:

A recognisable world. Memorable characters. Beautiful cards. A distinctive interface. Competitions that feel like events. And cards whose histories mean something because the player remembers how those histories happened.

That is the foundation Card Road should now build upon.

---

# 73. CURRENT BUILD SNAPSHOT (PWA v21)

**Title in code:** The Card Road — UI Geometry Fix v21  
**Form:** Portrait PWA (`index.html` + `manifest.webmanifest` + `service-worker.js` + art assets)  
**Cache name:** `card-road-pwa-v21-ui-geometry-fix`

**This pass changed only UI geometry**

- Date text moved into the parchment writing area.
- Location title/subtitle moved below the crest into the wooden panel.
- Noticeboard widened; live text constrained to three internal paper regions.
- Tomas shifted horizontally in Market only, to stop covering the noticeboard.

**Explicitly not in this pass:** artwork regeneration; NPC scaling; Nessa changes; presence-bar changes; gameplay changes; Journal/Time or bottom-navigation redesign.

**Already in the playable build**

- Locations: Market, Riverside, Inn, Card Club with production environment art.
- NPC standees: Tomas, Nessa, Bram, Elira (plus Tomas location placement).
- Journal tabs: Calendar, People, Cards, Card News, History.
- Collection, incoming challenges, local season, Saturday Card Club events.
- Physical-copy collection and ownership history inspection.
- CARDS array already stores C001–C120 Baseline V1 with `budget` = total.
- Player starter list and per-NPC starting collections are already assigned from that roster.
- Default NPC terms often use budget 86 (Bram/Elira often 92).

**Still a prototype surface**

- One large HTML file rather than a production architecture.
- TEST/DEBUG panels still on the home screen (reverse, hand visibility, combo, economy, advance world).
- Placeholder card names (`Design 001` …).
- No grandfather tutorial sequence yet as a finished opening.

---

# 74. IMPLEMENTATION GUIDANCE FOR A NEW OPERATOR

1. Import the roster using stable IDs **C001–C120**.
2. Preserve the exact directional orientation of each profile.
3. Store Total explicitly or calculate it from N+E+S+W and validate that it matches.
4. If deck cost remains identical to Total, use `deckCost` rather than overloading “budget”.
5. Attach future name/art/lore to the stable ID instead of replacing the ID.
6. Keep rarity/circulation metadata separate from numerical strength.
7. When balancing, version changes (Baseline V2) and preserve V1 for comparison.
8. Test suspected outliers in actual matches and deck-building before changing values.
9. Do not regenerate the entire roster for implementation convenience.
10. Do not invent historical rationale and present it as agreed canon. Structural interpretations should be labelled as interpretation.

The surviving project record preserves what was selected more reliably than the complete original reasoning discussion.

---

# Appendix A — Definitive Baseline V1 Roster

Authoritative row source: Roster V1 tab. Working names are placeholders only. Total is N+E+S+W and is the current card deck-cost value. Status for every row: **Baseline V1**.

| ID | Working name | N | E | S | W | Total | Geometry | Spread | Max | Min | Working role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C001 | Design 001 (TBD) | 3 | 5 | 3 | 3 | 14 | Balanced | 2 | 5 | 3 | Economy / specialist |
| C002 | Design 002 (TBD) | 1 | 1 | 6 | 6 | 14 | Adjacent Pair | 5 | 6 | 1 | Economy / specialist |
| C003 | Design 003 (TBD) | 7 | 1 | 5 | 1 | 14 | Opposite Pair | 6 | 7 | 1 | Economy / specialist |
| C004 | Design 004 (TBD) | 4 | 2 | 1 | 7 | 14 | Single-Side Specialist | 6 | 7 | 1 | Economy / specialist |
| C005 | Design 005 (TBD) | 2 | 4 | 6 | 2 | 14 | Asymmetric | 4 | 6 | 2 | Economy / specialist |
| C006 | Design 006 (TBD) | 1 | 10 | 2 | 1 | 14 | Extreme Specialist | 9 | 10 | 1 | Economy / specialist |
| C007 | Design 007 (TBD) | 3 | 4 | 4 | 4 | 15 | Balanced | 1 | 4 | 3 | Economy / specialist |
| C008 | Design 008 (TBD) | 6 | 1 | 1 | 7 | 15 | Adjacent Pair | 6 | 7 | 1 | Economy / specialist |
| C009 | Design 009 (TBD) | 7 | 1 | 6 | 1 | 15 | Opposite Pair | 6 | 7 | 1 | Economy / specialist |
| C010 | Design 010 (TBD) | 2 | 3 | 8 | 2 | 15 | Single-Side Specialist | 6 | 8 | 2 | Economy / specialist |
| C011 | Design 011 (TBD) | 5 | 7 | 1 | 2 | 15 | Asymmetric | 6 | 7 | 1 | Economy / specialist |
| C012 | Design 012 (TBD) | 1 | 10 | 3 | 1 | 15 | Extreme Specialist | 9 | 10 | 1 | Economy / specialist |
| C013 | Design 013 (TBD) | 1 | 1 | 6 | 7 | 15 | Adjacent Pair | 6 | 7 | 1 | Economy / specialist |
| C014 | Design 014 (TBD) | 5 | 4 | 4 | 3 | 16 | Balanced | 2 | 5 | 3 | Economy / specialist |
| C015 | Design 015 (TBD) | 1 | 1 | 7 | 7 | 16 | Adjacent Pair | 6 | 7 | 1 | Economy / specialist |
| C016 | Design 016 (TBD) | 1 | 7 | 2 | 6 | 16 | Opposite Pair | 6 | 7 | 1 | Economy / specialist |
| C017 | Design 017 (TBD) | 4 | 2 | 2 | 8 | 16 | Single-Side Specialist | 6 | 8 | 2 | Economy / specialist |
| C018 | Design 018 (TBD) | 2 | 5 | 7 | 2 | 16 | Asymmetric | 5 | 7 | 2 | Economy / specialist |
| C019 | Design 019 (TBD) | 10 | 1 | 1 | 4 | 16 | Extreme Specialist | 9 | 10 | 1 | Economy / specialist |
| C020 | Design 020 (TBD) | 7 | 7 | 1 | 1 | 16 | Adjacent Pair | 6 | 7 | 1 | Economy / specialist |
| C021 | Design 021 (TBD) | 7 | 1 | 7 | 1 | 16 | Opposite Pair | 6 | 7 | 1 | Economy / specialist |
| C022 | Design 022 (TBD) | 5 | 4 | 3 | 5 | 17 | Balanced | 2 | 5 | 3 | Flexible support |
| C023 | Design 023 (TBD) | 2 | 7 | 7 | 1 | 17 | Adjacent Pair | 6 | 7 | 1 | Flexible support |
| C024 | Design 024 (TBD) | 7 | 1 | 7 | 2 | 17 | Opposite Pair | 6 | 7 | 1 | Flexible support |
| C025 | Design 025 (TBD) | 2 | 2 | 8 | 5 | 17 | Single-Side Specialist | 6 | 8 | 2 | Flexible support |
| C026 | Design 026 (TBD) | 4 | 1 | 5 | 7 | 17 | Asymmetric | 6 | 7 | 1 | Flexible support |
| C027 | Design 027 (TBD) | 2 | 10 | 1 | 4 | 17 | Extreme Specialist | 9 | 10 | 1 | Flexible support |
| C028 | Design 028 (TBD) | 7 | 7 | 2 | 1 | 17 | Adjacent Pair | 6 | 7 | 1 | Flexible support |
| C029 | Design 029 (TBD) | 2 | 6 | 2 | 7 | 17 | Opposite Pair | 5 | 7 | 2 | Flexible support |
| C030 | Design 030 (TBD) | 3 | 5 | 5 | 4 | 17 | Balanced | 2 | 5 | 3 | Flexible support |
| C031 | Design 031 (TBD) | 4 | 6 | 4 | 4 | 18 | Balanced | 2 | 6 | 4 | Flexible support |
| C032 | Design 032 (TBD) | 8 | 2 | 2 | 6 | 18 | Adjacent Pair | 6 | 8 | 2 | Flexible support |
| C033 | Design 033 (TBD) | 6 | 2 | 8 | 2 | 18 | Opposite Pair | 6 | 8 | 2 | Flexible support |
| C034 | Design 034 (TBD) | 3 | 3 | 3 | 9 | 18 | Single-Side Specialist | 6 | 9 | 3 | Flexible support |
| C035 | Design 035 (TBD) | 3 | 3 | 7 | 5 | 18 | Asymmetric | 4 | 7 | 3 | Flexible support |
| C036 | Design 036 (TBD) | 1 | 9 | 7 | 1 | 18 | Extreme Specialist | 8 | 9 | 1 | Flexible support |
| C037 | Design 037 (TBD) | 6 | 8 | 2 | 2 | 18 | Adjacent Pair | 6 | 8 | 2 | Flexible support |
| C038 | Design 038 (TBD) | 2 | 8 | 2 | 6 | 18 | Opposite Pair | 6 | 8 | 2 | Flexible support |
| C039 | Design 039 (TBD) | 5 | 3 | 5 | 5 | 18 | Balanced | 2 | 5 | 3 | Flexible support |
| C040 | Design 040 (TBD) | 8 | 4 | 4 | 2 | 18 | Single-Side Specialist | 6 | 8 | 2 | Flexible support |
| C041 | Design 041 (TBD) | 6 | 5 | 4 | 4 | 19 | Balanced | 2 | 6 | 4 | Flexible support |
| C042 | Design 042 (TBD) | 2 | 2 | 7 | 8 | 19 | Adjacent Pair | 6 | 8 | 2 | Flexible support |
| C043 | Design 043 (TBD) | 2 | 8 | 2 | 7 | 19 | Opposite Pair | 6 | 8 | 2 | Flexible support |
| C044 | Design 044 (TBD) | 3 | 4 | 9 | 3 | 19 | Single-Side Specialist | 6 | 9 | 3 | Flexible support |
| C045 | Design 045 (TBD) | 4 | 7 | 5 | 3 | 19 | Asymmetric | 4 | 7 | 3 | Flexible support |
| C046 | Design 046 (TBD) | 10 | 1 | 1 | 7 | 19 | Extreme Specialist | 9 | 10 | 1 | Flexible support |
| C047 | Design 047 (TBD) | 6 | 2 | 3 | 8 | 19 | Adjacent Pair | 6 | 8 | 2 | Flexible support |
| C048 | Design 048 (TBD) | 8 | 2 | 7 | 2 | 19 | Opposite Pair | 6 | 8 | 2 | Flexible support |
| C049 | Design 049 (TBD) | 4 | 4 | 6 | 5 | 19 | Balanced | 2 | 6 | 4 | Flexible support |
| C050 | Design 050 (TBD) | 3 | 3 | 4 | 9 | 19 | Single-Side Specialist | 6 | 9 | 3 | Flexible support |
| C051 | Design 051 (TBD) | 5 | 5 | 2 | 7 | 19 | Asymmetric | 5 | 7 | 2 | Flexible support |
| C052 | Design 052 (TBD) | 5 | 5 | 4 | 6 | 20 | Balanced | 2 | 6 | 4 | Core |
| C053 | Design 053 (TBD) | 2 | 8 | 8 | 2 | 20 | Adjacent Pair | 6 | 8 | 2 | Core |
| C054 | Design 054 (TBD) | 8 | 3 | 7 | 2 | 20 | Opposite Pair | 6 | 8 | 2 | Core |
| C055 | Design 055 (TBD) | 3 | 3 | 9 | 5 | 20 | Single-Side Specialist | 6 | 9 | 3 | Core |
| C056 | Design 056 (TBD) | 7 | 5 | 5 | 3 | 20 | Asymmetric | 4 | 7 | 3 | Core |
| C057 | Design 057 (TBD) | 1 | 9 | 1 | 9 | 20 | Extreme Specialist | 8 | 9 | 1 | Core |
| C058 | Design 058 (TBD) | 8 | 2 | 2 | 8 | 20 | Adjacent Pair | 6 | 8 | 2 | Core |
| C059 | Design 059 (TBD) | 1 | 6 | 6 | 7 | 20 | Opposite Pair | 6 | 7 | 1 | Core |
| C060 | Design 060 (TBD) | 4 | 6 | 6 | 4 | 20 | Balanced | 2 | 6 | 4 | Core |
| C061 | Design 061 (TBD) | 5 | 9 | 3 | 3 | 20 | Single-Side Specialist | 6 | 9 | 3 | Core |
| C062 | Design 062 (TBD) | 5 | 7 | 3 | 5 | 20 | Asymmetric | 4 | 7 | 3 | Core |
| C063 | Design 063 (TBD) | 4 | 2 | 6 | 8 | 20 | Adjacent Pair | 6 | 8 | 2 | Core |
| C064 | Design 064 (TBD) | 4 | 6 | 5 | 6 | 21 | Balanced | 2 | 6 | 4 | Core |
| C065 | Design 065 (TBD) | 8 | 8 | 3 | 2 | 21 | Adjacent Pair | 6 | 8 | 2 | Core |
| C066 | Design 066 (TBD) | 7 | 2 | 8 | 4 | 21 | Opposite Pair | 6 | 8 | 2 | Core |
| C067 | Design 067 (TBD) | 9 | 3 | 3 | 6 | 21 | Single-Side Specialist | 6 | 9 | 3 | Core |
| C068 | Design 068 (TBD) | 7 | 5 | 4 | 5 | 21 | Asymmetric | 3 | 7 | 4 | Core |
| C069 | Design 069 (TBD) | 1 | 10 | 9 | 1 | 21 | Extreme Specialist | 9 | 10 | 1 | Core |
| C070 | Design 070 (TBD) | 2 | 3 | 8 | 8 | 21 | Adjacent Pair | 6 | 8 | 2 | Core |
| C071 | Design 071 (TBD) | 2 | 8 | 3 | 8 | 21 | Opposite Pair | 6 | 8 | 2 | Core |
| C072 | Design 072 (TBD) | 6 | 6 | 5 | 4 | 21 | Balanced | 2 | 6 | 4 | Core |
| C073 | Design 073 (TBD) | 3 | 9 | 6 | 3 | 21 | Single-Side Specialist | 6 | 9 | 3 | Core |
| C074 | Design 074 (TBD) | 5 | 7 | 4 | 5 | 21 | Asymmetric | 3 | 7 | 4 | Core |
| C075 | Design 075 (TBD) | 6 | 2 | 5 | 8 | 21 | Adjacent Pair | 6 | 8 | 2 | Core |
| C076 | Design 076 (TBD) | 6 | 6 | 5 | 5 | 22 | Balanced | 1 | 6 | 5 | Core |
| C077 | Design 077 (TBD) | 3 | 3 | 8 | 8 | 22 | Adjacent Pair | 5 | 8 | 3 | Core |
| C078 | Design 078 (TBD) | 8 | 3 | 8 | 3 | 22 | Opposite Pair | 5 | 8 | 3 | Core |
| C079 | Design 079 (TBD) | 3 | 9 | 6 | 4 | 22 | Single-Side Specialist | 6 | 9 | 3 | Core |
| C080 | Design 080 (TBD) | 8 | 4 | 2 | 8 | 22 | Adjacent Pair | 6 | 8 | 2 | Core |
| C081 | Design 081 (TBD) | 10 | 10 | 1 | 1 | 22 | Extreme Specialist | 9 | 10 | 1 | Core |
| C082 | Design 082 (TBD) | 8 | 8 | 3 | 3 | 22 | Adjacent Pair | 5 | 8 | 3 | Core |
| C083 | Design 083 (TBD) | 3 | 7 | 3 | 9 | 22 | Opposite Pair | 6 | 9 | 3 | Core |
| C084 | Design 084 (TBD) | 5 | 5 | 7 | 5 | 22 | Balanced | 2 | 7 | 5 | Core |
| C085 | Design 085 (TBD) | 10 | 4 | 4 | 4 | 22 | Single-Side Specialist | 6 | 10 | 4 | Core |
| C086 | Design 086 (TBD) | 7 | 2 | 6 | 7 | 22 | Adjacent Pair | 5 | 7 | 2 | Core |
| C087 | Design 087 (TBD) | 5 | 6 | 7 | 5 | 23 | Balanced | 2 | 7 | 5 | Premium |
| C088 | Design 088 (TBD) | 8 | 3 | 3 | 9 | 23 | Adjacent Pair | 6 | 9 | 3 | Premium |
| C089 | Design 089 (TBD) | 3 | 9 | 3 | 8 | 23 | Opposite Pair | 6 | 9 | 3 | Premium |
| C090 | Design 090 (TBD) | 10 | 4 | 5 | 4 | 23 | Single-Side Specialist | 6 | 10 | 4 | Premium |
| C091 | Design 091 (TBD) | 8 | 9 | 3 | 3 | 23 | Adjacent Pair | 6 | 9 | 3 | Premium |
| C092 | Design 092 (TBD) | 1 | 2 | 10 | 10 | 23 | Extreme Specialist | 9 | 10 | 1 | Premium |
| C093 | Design 093 (TBD) | 5 | 2 | 8 | 8 | 23 | Adjacent Pair | 6 | 8 | 2 | Premium |
| C094 | Design 094 (TBD) | 7 | 3 | 9 | 4 | 23 | Opposite Pair | 6 | 9 | 3 | Premium |
| C095 | Design 095 (TBD) | 6 | 5 | 5 | 7 | 23 | Balanced | 2 | 7 | 5 | Premium |
| C096 | Design 096 (TBD) | 4 | 10 | 5 | 4 | 23 | Single-Side Specialist | 6 | 10 | 4 | Premium |
| C097 | Design 097 (TBD) | 5 | 7 | 6 | 6 | 24 | Balanced | 2 | 7 | 5 | Premium |
| C098 | Design 098 (TBD) | 9 | 3 | 3 | 9 | 24 | Adjacent Pair | 6 | 9 | 3 | Premium |
| C099 | Design 099 (TBD) | 8 | 4 | 9 | 3 | 24 | Opposite Pair | 6 | 9 | 3 | Premium |
| C100 | Design 100 (TBD) | 10 | 6 | 4 | 4 | 24 | Single-Side Specialist | 6 | 10 | 4 | Premium |
| C101 | Design 101 (TBD) | 3 | 3 | 9 | 9 | 24 | Adjacent Pair | 6 | 9 | 3 | Premium |
| C102 | Design 102 (TBD) | 2 | 10 | 2 | 10 | 24 | Extreme Specialist | 8 | 10 | 2 | Premium |
| C103 | Design 103 (TBD) | 3 | 9 | 9 | 3 | 24 | Adjacent Pair | 6 | 9 | 3 | Premium |
| C104 | Design 104 (TBD) | 6 | 8 | 2 | 8 | 24 | Opposite Pair | 6 | 8 | 2 | Premium |
| C105 | Design 105 (TBD) | 7 | 5 | 5 | 7 | 24 | Balanced | 2 | 7 | 5 | Premium |
| C106 | Design 106 (TBD) | 6 | 6 | 6 | 7 | 25 | Balanced | 1 | 7 | 6 | Marquee |
| C107 | Design 107 (TBD) | 3 | 9 | 9 | 4 | 25 | Adjacent Pair | 6 | 9 | 3 | Marquee |
| C108 | Design 108 (TBD) | 9 | 4 | 9 | 3 | 25 | Opposite Pair | 6 | 9 | 3 | Marquee |
| C109 | Design 109 (TBD) | 10 | 7 | 4 | 4 | 25 | Single-Side Specialist | 6 | 10 | 4 | Marquee |
| C110 | Design 110 (TBD) | 4 | 3 | 9 | 9 | 25 | Adjacent Pair | 6 | 9 | 3 | Marquee |
| C111 | Design 111 (TBD) | 1 | 10 | 4 | 10 | 25 | Extreme Specialist | 9 | 10 | 1 | Marquee |
| C112 | Design 112 (TBD) | 9 | 4 | 3 | 9 | 25 | Adjacent Pair | 6 | 9 | 3 | Marquee |
| C113 | Design 113 (TBD) | 2 | 8 | 7 | 8 | 25 | Opposite Pair | 6 | 8 | 2 | Marquee |
| C114 | Design 114 (TBD) | 5 | 7 | 7 | 7 | 26 | Balanced | 2 | 7 | 5 | Marquee |
| C115 | Design 115 (TBD) | 9 | 9 | 3 | 5 | 26 | Adjacent Pair | 6 | 9 | 3 | Marquee |
| C116 | Design 116 (TBD) | 9 | 4 | 9 | 4 | 26 | Opposite Pair | 5 | 9 | 4 | Marquee |
| C117 | Design 117 (TBD) | 7 | 5 | 4 | 10 | 26 | Single-Side Specialist | 6 | 10 | 4 | Marquee |
| C118 | Design 118 (TBD) | 3 | 9 | 9 | 5 | 26 | Adjacent Pair | 6 | 9 | 3 | Marquee |
| C119 | Design 119 (TBD) | 4 | 2 | 10 | 10 | 26 | Extreme Specialist | 8 | 10 | 2 | Marquee |
| C120 | Design 120 (TBD) | 7 | 3 | 8 | 8 | 26 | Adjacent Pair | 5 | 8 | 3 | Marquee |

---

*End of living design bible. Next recommended work: copy the v21 PWA into this folder as the playable source of truth, then continue from presentation and world — not new match complexity.*
