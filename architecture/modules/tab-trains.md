# MOD-3: Trains Tab

## Requirement Coverage

| REQ ID | Requirement | Implementation |
|--------|-------------|----------------|
| REQ-3 | Trains tab with all four TGV journeys; seat number findable in under 5 seconds | Four journey cards in `<section id="tab-trains">`, chronological order |
| REQ-3.1 | Outbound Group 1 — Jul 4, TGV 6109, Coach 8, four travelers | Journey card 1 with seat table |
| REQ-3.2 | Outbound Group 2 — Jul 5, TGV 6109, Coach 15, two travelers | Journey card 2 with seat table |
| REQ-3.3 | Return Emmanuelle & Lukas — Jul 10, TGV 6120, Coach 12 | Journey card 3 with seat table |
| REQ-3.4 | Return Main Group — Jul 11, TGV 6122, Coach 12, four travelers | Journey card 4 with seat table |

---

## Responsibility

Renders the Trains tab panel. Contains four journey cards, one per TGV booking, in chronological order. Each card gives a traveler everything needed to board: train number, departure/arrival, coach, board-by time, and their personal seat number and position.

All content is static HTML. No JavaScript required beyond App Shell tab routing.

---

## Panel Structure

```
<section id="tab-trains">
  ├── Section Header
  ├── Journey Card 1 — Outbound Group 1 (Jul 4)
  │     ├── Journey header (train, route, direction)
  │     ├── Logistics row (departs, arrives, duration, class, coach, board-by)
  │     └── Seat table (4 travelers)
  ├── Journey Card 2 — Outbound Group 2 (Jul 5)
  │     ├── Journey header
  │     ├── Logistics row
  │     └── Seat table (2 travelers)
  ├── Journey Card 3 — Return Emmanuelle & Lukas (Jul 10)
  │     ├── Journey header
  │     ├── Logistics row
  │     └── Seat table (2 travelers)
  ├── Journey Card 4 — Return Main Group (Jul 11)
  │     ├── Journey header
  │     ├── Logistics row
  │     └── Seat table (4 travelers)
  └── Transfer Note
</section>
```

---

## Journey Card Template

Each of the four journey cards follows the same structure:

```html
<div class="bg-white rounded-xl shadow-sm mb-4 overflow-hidden">
  <!-- Card header band -->
  <div class="bg-terracotta px-4 py-3">
    <p class="text-white text-xs font-semibold uppercase tracking-wide">{DIRECTION} — {DATE}</p>
    <p class="text-white font-bold text-base">TGV INOUI {TRAIN_NO}</p>
    <p class="text-red-100 text-sm">{ORIGIN} → {DESTINATION}</p>
  </div>

  <!-- Logistics row -->
  <div class="px-4 py-3 grid grid-cols-3 gap-2 text-center border-b border-gray-100">
    <div>
      <p class="text-xs text-gray-400">Departs</p>
      <p class="font-semibold text-sm">{DEPARTS}</p>
    </div>
    <div>
      <p class="text-xs text-gray-400">Arrives</p>
      <p class="font-semibold text-sm">{ARRIVES}</p>
    </div>
    <div>
      <p class="text-xs text-gray-400">Duration</p>
      <p class="font-semibold text-sm">{DURATION}</p>
    </div>
  </div>

  <!-- Class / Coach / Board-by -->
  <div class="px-4 py-2 flex gap-4 text-sm text-gray-600 border-b border-gray-100">
    <span>{CLASS}</span>
    <span>Coach {COACH}</span>
    <span class="text-terracotta font-medium">Board by {BOARD_BY}</span>
  </div>

  <!-- Seat table -->
  <div class="table-scroll">
    <table class="text-sm w-full border-collapse">
      <thead>
        <tr class="bg-gray-50">
          <th class="px-3 py-2 text-left text-gray-500 font-medium">Traveler</th>
          <th class="px-3 py-2 text-left text-gray-500 font-medium">Seat</th>
          <th class="px-3 py-2 text-left text-gray-500 font-medium">Position</th>
        </tr>
      </thead>
      <tbody>
        {SEAT_ROWS}
      </tbody>
    </table>
  </div>
</div>
```

---

## Journey Card Data

### Card 1 — Outbound Group 1: Saturday July 4

| Field | Value |
|-------|-------|
| Direction | Outbound |
| Train | TGV INOUI 6109 |
| Route | Paris Gare de Lyon → Avignon TGV |
| Departs | 10:38 AM |
| Arrives | 1:19 PM |
| Duration | 2h 41min |
| Class | 2nd Class |
| Coach | 8 |
| Board by | 10:36 AM |

Seat table:

| Traveler | Seat | Position |
|---|---|---|
| Olivier Gers | 813 | Lower deck, Window |
| Dana Gers | 806 | Lower deck, Corridor |
| Emmanuelle Gers | 807 | Lower deck, Window |
| Lukas Stachtiaris | 812 | Lower deck, Corridor |

---

### Card 2 — Outbound Group 2: Sunday July 5

| Field | Value |
|-------|-------|
| Direction | Outbound |
| Train | TGV INOUI 6109 |
| Route | Paris Gare de Lyon → Avignon TGV |
| Departs | 10:38 AM |
| Arrives | 1:19 PM |
| Duration | 2h 41min |
| Class | 2nd Class |
| Coach | 15 |
| Board by | 10:36 AM |

Seat table:

| Traveler | Seat | Position |
|---|---|---|
| Alexandra Gers | 559 | Upper deck, Window |
| Colby Gates | 558 | Upper deck, Corridor |

---

### Card 3 — Return: Emmanuelle & Lukas, Friday July 10

| Field | Value |
|-------|-------|
| Direction | Return |
| Train | TGV INOUI 6120 |
| Route | Avignon TGV → Paris Gare de Lyon |
| Departs | 2:41 PM |
| Arrives | 5:22 PM |
| Duration | 2h 41min |
| Class | 1st Class |
| Coach | 12 |
| Board by | 2:39 PM |

Seat table:

| Traveler | Seat | Position |
|---|---|---|
| Emmanuelle Gers | 272 | Upper deck, Window |
| Lukas Stachtiaris | 271 | Upper deck, Corridor |

---

### Card 4 — Return: Main Group, Saturday July 11

| Field | Value |
|-------|-------|
| Direction | Return |
| Train | TGV INOUI 6122 |
| Route | Avignon TGV → Paris Gare de Lyon |
| Departs | 3:37 PM |
| Arrives | 6:22 PM |
| Duration | 2h 45min |
| Class | 1st Class |
| Coach | 12 |
| Board by | 3:35 PM |

Seat table:

| Traveler | Seat | Position |
|---|---|---|
| Olivier Gers | 244 | Upper deck, Corridor |
| Dana Gers | 247 | Upper deck, Corridor |
| Alexandra Gers | 248 | Upper deck, Window |
| Colby Gates | 245 | Upper deck, Window |

---

## Transfer Note

Displayed below all four cards as a callout block.

```html
<div class="bg-lavender/10 border border-lavender/30 rounded-xl px-4 py-3 text-sm text-gray-700">
  <p class="font-semibold text-lavender mb-1">Avignon TGV → St. Rémy</p>
  <p>The TGV station is outside the city center. Allow <strong>35–40 minutes</strong> by taxi
  or pre-arranged car to reach the house. Book transfers in advance for July.</p>
</div>
```

---

## Inputs

| Input | Source |
|-------|--------|
| `<section id="tab-trains">` mount point | MOD-1 App Shell |
| Tailwind color classes | MOD-1 App Shell |
| `table-scroll` CSS class | MOD-1 App Shell |

---

## Outputs

None. This module produces no outputs consumed by other modules.

---

## Dependencies

| Dependency | Module |
|------------|--------|
| Tab panel mount point and routing | MOD-1 App Shell |
| Tailwind custom color config | MOD-1 App Shell |

---

## Notes

- All four seat tables are wrapped in `div.table-scroll` so they scroll horizontally on viewports narrower than the table — required by REQ-9.
- Seat numbers are the primary information hierarchy — rendered in a larger, bolder font than traveler name to aid fast scanning.
- No JavaScript in this module.
