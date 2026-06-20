# MOD-5: Guide Tab

## Requirement Coverage

| REQ ID | Requirement | Implementation |
|--------|-------------|----------------|
| REQ-5 | Guide tab with six sub-sections, scannable on mobile | `<section id="tab-guide">` with seven collapsible or stacked cards |
| REQ-5.1 | Fine dining: L'Auberge, de Tourrel, Domaine de Baumanière | Fine Dining card — three entries with Michelin notes |
| REQ-5.2 | Casual: Edú (full details), Olga, Lou Patio, Canto Cigalo, Bienbon, Basta Cosi! | Casual Restaurants card — six entries, TheFork ratings |
| REQ-5.3 | Bakery: Terre et Blé — address, phone, website, go-early note | Bakery card |
| REQ-5.4 | Saturday Market — dates, timing, what to find, practical tips | Market card |
| REQ-5.5 | Things to Do — eight attractions in two groups with drive times | Activities card |
| REQ-5.6 | FIFA World Cup — fan zones, local viewing, time-zone tip | World Cup card |
| REQ-5.7 | Practical Tips — weather, language, cash, rosé, driving, restaurant timing | Tips card |

---

## Responsibility

Renders the Guide tab panel. Contains the full St. Rémy-de-Provence local guide in a vertical stack of section cards. Each card is a self-contained block covering one topic. Content is dense but structured for mobile scanning — section headers are large, individual entries are compact.

All content is static HTML. No JavaScript required beyond App Shell tab routing.

---

## Panel Structure

```
<section id="tab-guide">
  ├── Section Header
  ├── Card: Fine Dining (REQ-5.1)
  ├── Card: Casual Restaurants (REQ-5.2)
  ├── Card: Bakery — Terre et Blé (REQ-5.3)
  ├── Card: Saturday Market (REQ-5.4)
  ├── Card: Things to Do (REQ-5.5)
  ├── Card: FIFA World Cup 2026 (REQ-5.6)
  └── Card: Practical Tips (REQ-5.7)
</section>
```

---

## Card Template

All guide cards share this shell:

```html
<div class="bg-white rounded-xl shadow-sm mb-4 overflow-hidden">
  <div class="bg-{ACCENT_COLOR} px-4 py-3">
    <p class="text-white font-bold text-base">{SECTION_TITLE}</p>
  </div>
  <div class="px-4 py-4 space-y-4 text-sm">
    {CONTENT}
  </div>
</div>
```

Accent colors per section: terracotta (Fine Dining), terracotta (Casual), olive (Bakery), olive (Market), lavender (Things to Do), terracotta (World Cup), gray-700 (Practical Tips).

---

## Card 1: Fine Dining (REQ-5.1)

Three Michelin-starred entries. Each entry shows name, star count, one-line description, and reservation urgency.

```
L'Auberge de Saint-Rémy
  ★ Michelin · Chef Fanny Rey
  The benchmark for a special-occasion dinner in St. Rémy.
  Reserve well in advance for July.

Restaurant de Tourrel
  ★ Michelin · 17th-century mansion
  Tasting menus and exceptional wine list. Book early.

Domaine de Baumanière
  ★★ Michelin · Les Baux-de-Provence (20 min)
  One of the landmark addresses in French gastronomy.
  Worth the drive. Dress accordingly.
```

---

## Card 2: Casual Restaurants (REQ-5.2)

Six entries. Edú gets full detail block (address, phone, hours, closed days). Others get name, one-line descriptor, and TheFork rating where available.

```
Edú
  17 Av. Albert Schweitzer, 13210 Saint-Rémy-de-Provence
  Phone: +33 4 90 20 94 21 · edu-restaurant.com
  Mediterranean plates, natural wines, terrace around a pond.
  Fooding and Gault & Millau listed. Reservations recommended.
  ⛔ CLOSED Sunday and Monday
  Open Tue–Sat: Lunch 12:00–1:30 PM · Dinner 7:00–9:00 PM
  Own parking on site.

Olga by le Bistrot Découverte
  Beloved local bistro. TheFork 8.9

Restaurant Lou Patio (Hotel le Saint-Rémy)
  Garden terrace dining. TheFork 8.9

Bistrot Canto Cigalo (Le Vallon de Valrugues)
  Classic Provençal setting in a beautiful hotel. TheFork 8.6

Bienbon
  Creative vegetarian and vegan-friendly menu.

Basta Cosi!
  Casual Italian for a relaxed evening.
```

---

## Card 3: Bakery — Terre et Blé (REQ-5.3)

```
Terre et Blé
  ZAC de la Gare, 24 Av. Albin Gilles
  13210 Saint-Rémy-de-Provence
  +33 4 90 89 72 30 · terredeble.com

  100% sourdough, wood-fired, organic, grain-to-table.
  Also serves a daily changing lunch menu.
  The best bread in Saint-Rémy — go early, it sells out.
  Open on Mondays (rare for the area).
```

---

## Card 4: Saturday Market (REQ-5.4)

```
Every Saturday morning through the old town.
Boulevard Mirabeau and surrounding streets.
Family dates: July 5 and July 11.

TIMING
  8:30–9:00 AM — bread and pastries before they sell out
  10:00–11:00 AM — full market in swing

FIND
  Fresh produce, olives, local goat cheese, honey, tapenade,
  lavender, Provençal fabrics, ceramics, local crafts.

PRACTICAL
  Cash useful for smaller vendors.
  Park outside the center and walk in — no cars inside during market hours.
```

---

## Card 5: Things to Do (REQ-5.5)

Two groups: Near (under 30 min) and Day Trips (30–60 min). Eight entries total.

```
NEAR ST. RÉMY — UNDER 30 MIN

Les Baux-de-Provence · 20 min
  Hilltop village on white limestone cliffs. Allow 2–3 hours.
  Go before 10 AM or late afternoon to beat July crowds.

Saint-Paul-de-Mausole · walkable
  Van Gogh's asylum. Gardens open to visitors. Quiet and moving.

Glanum (Les Antiques) · walkable to road
  Roman ruins at the southern edge of town. Triumphal arch and
  mausoleum visible from the road for free. Site worth an hour.

Les Alpilles Natural Park · from town
  Cycling and hiking through dramatic white limestone hills.
  Bike rental available in town.

---

DAY TRIPS — 30–60 MIN

Arles · 35 min
  Roman amphitheater still in use. Van Gogh trail. Excellent
  restaurant scene. Worth a full day.

Avignon · 25 min
  The Palais des Papes, the Pont d'Avignon, great cafés.
  Easy half-day trip.

Luberon · 45–60 min
  Gordes, Roussillon, Bonnieux. Plan a full day.
  Gordes at sunset is one of the best views in France.

Camargue · 45 min
  Pink flamingos, white Camargue horses, salt flats.
  Best visited in the early morning.
```

---

## Card 6: FIFA World Cup 2026 (REQ-5.6)

```
The family's stay (Jul 4–11) covers the Round of 16 (Jul 4–7)
and Quarterfinals (Jul 9–11).

FAN ZONES WITH GIANT SCREENS
  Avignon · 25 min
  Arles · 35 min
  Aix-en-Provence · 40 min
  Check fanzone-coupedumonde.fr for confirmed locations.

IN ST. RÉMY
  Cafés and bars on Place de la République will have screens
  for any France match.

TIME ZONES
  A 3:00 PM ET kickoff = 9:00 PM local — ideal for a terrace.

CHECK BRACKET
  Confirm France's position the week before departure.
  Potential France quarterfinal matches: July 9, 10, or 11.
```

---

## Card 7: Practical Tips (REQ-5.7)

Seven compact tip rows, one per topic:

```
Weather
  30–35°C and full sun in July. Carry water everywhere.
  Siesta (1–4 PM) is real — some shops close.

Language
  French always appreciated. English spoken in tourist contexts.
  Bonjour before any request goes a very long way.

Cash
  Useful for markets, Terre et Blé, and parking meters.
  Restaurants and larger shops take cards.

Rosé Wine
  Provence produces exceptional rosé. Ask for something local.
  Domaine Hauvette, Trévallon, and Romanin are nearby estates.

Driving
  A car is essential from St. Rémy. Village streets are narrow.
  Roundabouts everywhere. Drive slowly and calmly.

Restaurant Timing
  Dinner: most restaurants open no earlier than 7:30 PM.
  Lunch: service typically ends by 1:30 PM. Plan accordingly.

Reservations
  July is peak season. Book Michelin restaurants now.
  Book Edú at least a week in advance.
```

---

## Inputs

| Input | Source |
|-------|--------|
| `<section id="tab-guide">` mount point | MOD-1 App Shell |
| Tailwind color classes (`terracotta`, `lavender`, `olive`) | MOD-1 App Shell |

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

- The Guide tab is the longest panel. It is a vertical scroll — no pagination or accordion is required, keeping the implementation simple and the content always discoverable.
- Edú's `CLOSED Sunday and Monday` warning is styled prominently (red badge or bold uppercase) because it is the most likely scheduling mistake a family member could make.
- No JavaScript in this module.
