# MOD-2: Home Tab

## Requirement Coverage

| REQ ID | Requirement | Implementation |
|--------|-------------|----------------|
| REQ-2 | Home tab: traveler list, timeline, Google Maps house link | Static HTML inside `<section id="tab-home">` |
| REQ-7 | Flights reference: DL 220 outbound, DL 221 return, note about other travelers | Flights section at bottom of Home tab panel |

---

## Responsibility

Renders the Home tab panel — the first thing a user sees when the app opens. Contains all trip-level context: who is on the trip, when each leg happens, where the house is, and the confirmed Olivier/Dana flight details.

All content is static HTML. No JavaScript is required in this module beyond what the App Shell provides (tab routing).

---

## Panel Structure

```
<section id="tab-home">
  ├── Trip Header
  ├── Travelers Section
  ├── Timeline Section
  ├── House Address Section   ← includes Google Maps button
  └── Flights Reference Section
</section>
```

---

## Sections

### Trip Header

```html
<header class="mb-6">
  <h1 class="text-2xl font-bold text-terracotta">France Family Trip</h1>
  <p class="text-olive font-medium">St. Rémy-de-Provence · July 2026</p>
</header>
```

---

### Travelers Section

Displays all seven travelers as a simple list.

```html
<section class="mb-6">
  <h2 class="text-lg font-semibold text-lavender mb-2">Travelers</h2>
  <ul class="space-y-1 text-sm">
    <li>Olivier Gers</li>
    <li>Dana Gers</li>
    <li>Emmanuelle Gers <span class="text-gray-400">(daughter)</span></li>
    <li>Lukas Stachtiaris <span class="text-gray-400">(Emmanuelle's partner)</span></li>
    <li>Alexandra Gers <span class="text-gray-400">(daughter)</span></li>
    <li>Colby Gates <span class="text-gray-400">(Alexandra's partner)</span></li>
    <li>Frederick Gers <span class="text-gray-400">(Olivier's brother)</span></li>
  </ul>
</section>
```

---

### Timeline Section

Eight-row table covering the full trip from departure to return.

```html
<section class="mb-6">
  <h2 class="text-lg font-semibold text-lavender mb-2">Trip Timeline</h2>
  <div class="table-scroll">
    <table class="text-sm w-full border-collapse">
      <thead>
        <tr class="bg-terracotta text-white">
          <th class="px-3 py-2 text-left whitespace-nowrap">Date</th>
          <th class="px-3 py-2 text-left">Event</th>
        </tr>
      </thead>
      <tbody>
        <tr><td class="px-3 py-2 font-medium whitespace-nowrap">Jul 2</td>
            <td class="px-3 py-2">Olivier + Dana depart SLC on DL 220</td></tr>
        <tr class="bg-cream"><td class="px-3 py-2 font-medium whitespace-nowrap">Jul 3</td>
            <td class="px-3 py-2">Arrive CDG ~9:30 AM. Full group assembles at Hotel Belmont Paris around lunch</td></tr>
        <tr><td class="px-3 py-2 font-medium whitespace-nowrap">Jul 4</td>
            <td class="px-3 py-2">Olivier, Dana, Emmanuelle, Lukas: TGV to Avignon then St. Rémy</td></tr>
        <tr class="bg-cream"><td class="px-3 py-2 font-medium whitespace-nowrap">Jul 5</td>
            <td class="px-3 py-2">Alexandra, Colby: TGV to Avignon then St. Rémy (extra Paris night)</td></tr>
        <tr><td class="px-3 py-2 font-medium whitespace-nowrap">Jul 5–11</td>
            <td class="px-3 py-2">Full family at the house in St. Rémy-de-Provence</td></tr>
        <tr class="bg-cream"><td class="px-3 py-2 font-medium whitespace-nowrap">Jul 10</td>
            <td class="px-3 py-2">Emmanuelle + Lukas: TGV return to Paris</td></tr>
        <tr><td class="px-3 py-2 font-medium whitespace-nowrap">Jul 11</td>
            <td class="px-3 py-2">Olivier, Dana, Alexandra, Colby: TGV return to Paris</td></tr>
        <tr class="bg-cream"><td class="px-3 py-2 font-medium whitespace-nowrap">Jul 12</td>
            <td class="px-3 py-2">Olivier + Dana: DL 221 CDG to SLC</td></tr>
      </tbody>
    </table>
  </div>
</section>
```

---

### House Address Section

Prominent card with one-tap Google Maps button. This is the primary navigation aid for the whole trip.

```html
<section class="mb-6">
  <h2 class="text-lg font-semibold text-lavender mb-2">The House</h2>
  <div class="bg-white rounded-xl shadow-sm p-4 border-l-4 border-terracotta">
    <p class="font-semibold text-gray-800">314 Chemin de Carraire de la Crau</p>
    <p class="text-gray-600 mb-3">13210 Saint-Rémy-de-Provence</p>
    <a href="https://maps.google.com/?q=314+Chemin+de+Carraire+de+la+Crau,+13210+Saint-Rémy-de-Provence"
       class="inline-block bg-terracotta text-white text-sm font-medium px-4 py-2 rounded-lg">
      Open in Maps
    </a>
  </div>
</section>
```

The `<a>` tag with a `maps.google.com/?q=` URL opens the native Maps app on iOS and Android when tapped in a mobile browser.

---

### Flights Reference Section

Displays Olivier and Dana's confirmed Delta flights. Includes a note that all other travelers have separate arrangements and will post to the Notes board.

```html
<section class="mb-6">
  <h2 class="text-lg font-semibold text-lavender mb-2">Flights</h2>

  <div class="space-y-3">
    <!-- Outbound -->
    <div class="bg-white rounded-xl shadow-sm p-4">
      <p class="text-xs font-semibold text-olive uppercase tracking-wide mb-1">Outbound — July 2</p>
      <p class="font-semibold">Delta DL 220 · SLC → CDG</p>
      <p class="text-sm text-gray-600">Departs ~3:25 PM MDT · Arrives ~9:30 AM CEST (Jul 3)</p>
      <p class="text-sm text-gray-600">Terminal 2E · Airbus A330-300 · Non-stop</p>
      <p class="text-sm text-gray-500 mt-1">Passengers: Olivier Gers, Dana Gers</p>
    </div>

    <!-- Return -->
    <div class="bg-white rounded-xl shadow-sm p-4">
      <p class="text-xs font-semibold text-olive uppercase tracking-wide mb-1">Return — July 12</p>
      <p class="font-semibold">Delta DL 221 · CDG → SLC</p>
      <p class="text-sm text-gray-500 mt-1">Passengers: Olivier Gers, Dana Gers</p>
      <p class="text-sm text-gray-400 italic">Departure time: confirm from booking confirmation</p>
    </div>

    <!-- Other travelers note -->
    <p class="text-xs text-gray-400 px-1">
      Emmanuelle, Lukas, Alexandra, Colby, and Frederick have separate flight arrangements
      — post details to the Notes board so everyone has them.
    </p>
  </div>
</section>
```

---

## Inputs

| Input | Source |
|-------|--------|
| `<section id="tab-home">` mount point | MOD-1 App Shell |
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

- The Google Maps URL uses `?q=` query parameter — works on iOS Safari, Android Chrome, and desktop browsers. On mobile it deep-links to the native Maps app.
- `table-scroll` wrapper (defined in App Shell `<style>`) enables horizontal scroll on the timeline table if the viewport is narrower than the table content.
- No JavaScript in this module.
