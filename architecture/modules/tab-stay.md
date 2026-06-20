# MOD-4: Stay Tab

## Requirement Coverage

| REQ ID | Requirement | Implementation |
|--------|-------------|----------------|
| REQ-4 | Stay tab with all accommodation details | Three accommodation cards in `<section id="tab-stay">` |
| REQ-4.1 | Hotel Le Belmont Paris — outbound night Jul 3 | Card 1: address, metro, dates, Alexandra/Colby extra night note |
| REQ-4.2 | The House in St. Rémy — Jul 5–11, one-tap Google Maps | Card 2: address with Maps button |
| REQ-4.3 | Return Paris hotel TBD — HotelTonight, post to Notes board | Card 3: note explaining booking plan |

---

## Responsibility

Renders the Stay tab panel. Contains three accommodation cards in trip order. Gives every family member the address and key details for each place they'll sleep, without requiring any app interaction to locate the information.

All content is static HTML. No JavaScript required beyond App Shell tab routing.

---

## Panel Structure

```
<section id="tab-stay">
  ├── Section Header
  ├── Card 1 — Hotel Le Belmont Paris (Jul 3)
  ├── Card 2 — The House in St. Rémy (Jul 5–11)   ← Google Maps button
  └── Card 3 — Return Paris Hotel TBD (Jul 11)
</section>
```

---

## Card 1: Hotel Le Belmont Paris (Outbound, July 3)

```html
<div class="bg-white rounded-xl shadow-sm mb-4 overflow-hidden">
  <div class="bg-terracotta px-4 py-3">
    <p class="text-red-100 text-xs font-semibold uppercase tracking-wide">Outbound — July 3</p>
    <p class="text-white font-bold text-base">Hotel Le Belmont Paris</p>
  </div>
  <div class="px-4 py-4 space-y-2 text-sm">
    <div>
      <p class="text-gray-500 text-xs uppercase tracking-wide mb-0.5">Address</p>
      <p class="font-medium">30 Rue de Bassano, 75116 Paris</p>
    </div>
    <div>
      <p class="text-gray-500 text-xs uppercase tracking-wide mb-0.5">Metro</p>
      <p>George V (Line 1) — 5 min walk to Champs-Élysées</p>
    </div>
    <div>
      <p class="text-gray-500 text-xs uppercase tracking-wide mb-0.5">Dates</p>
      <p>Check-in July 3 · Check-out July 4 morning</p>
    </div>
    <div>
      <p class="text-gray-500 text-xs uppercase tracking-wide mb-0.5">Neighborhood</p>
      <p>4-star hotel, Golden Triangle</p>
    </div>
    <p class="text-gray-400 text-xs border-t border-gray-100 pt-2 mt-2">
      Full group assembles here around lunchtime July 3.<br>
      Alexandra and Colby stay one additional night (July 4) and depart the morning of July 5 for the train.
    </p>
  </div>
</div>
```

---

## Card 2: The House in St. Rémy (July 5–11)

This is the most critical card — the house address is the primary navigation target for the whole trip. The Google Maps button uses the same `maps.google.com/?q=` URL as the Home tab (MOD-2).

```html
<div class="bg-white rounded-xl shadow-sm mb-4 overflow-hidden">
  <div class="bg-olive px-4 py-3">
    <p class="text-green-100 text-xs font-semibold uppercase tracking-wide">Jul 5–11</p>
    <p class="text-white font-bold text-base">The House — St. Rémy-de-Provence</p>
  </div>
  <div class="px-4 py-4">
    <div class="mb-3">
      <p class="text-gray-500 text-xs uppercase tracking-wide mb-0.5">Address</p>
      <p class="font-semibold text-gray-800">314 Chemin de Carraire de la Crau</p>
      <p class="text-gray-600">13210 Saint-Rémy-de-Provence</p>
    </div>
    <a href="https://maps.google.com/?q=314+Chemin+de+Carraire+de+la+Crau,+13210+Saint-Rémy-de-Provence"
       class="inline-block bg-terracotta text-white text-sm font-medium px-4 py-2 rounded-lg">
      Open in Maps
    </a>
  </div>
</div>
```

---

## Card 3: Return Paris Hotel TBD (July 11)

```html
<div class="bg-white rounded-xl shadow-sm mb-4 overflow-hidden">
  <div class="bg-lavender px-4 py-3">
    <p class="text-purple-100 text-xs font-semibold uppercase tracking-wide">Return — July 11</p>
    <p class="text-white font-bold text-base">Paris Hotel — TBD</p>
  </div>
  <div class="px-4 py-4 text-sm space-y-2">
    <p>Olivier + Dana · Night of July 11</p>
    <p class="text-gray-600">Train arrives Paris Gare de Lyon at <strong>6:22 PM</strong>.</p>
    <p class="text-gray-600">
      Hotel will be booked day-of or the day before via
      <strong>HotelTonight</strong>.
    </p>
    <p class="text-gray-400 text-xs border-t border-gray-100 pt-2 mt-2">
      Once booked, Olivier posts the hotel name and address to the Family Notes board
      so everyone has it.
    </p>
  </div>
</div>
```

---

## Inputs

| Input | Source |
|-------|--------|
| `<section id="tab-stay">` mount point | MOD-1 App Shell |
| Tailwind color classes (`terracotta`, `lavender`, `olive`, `cream`) | MOD-1 App Shell |

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

- The Google Maps link in Card 2 is identical to the one in MOD-2 (Home tab). Both point to the same `?q=` URL. If the address ever changes it must be updated in both places.
- Cards are colored by role: terracotta for outbound Paris (journey-start feel), olive for the house (nature/Provence), lavender for return Paris (winding-down feel).
- No JavaScript in this module.
