# Architecture
## France Family Trip App — St. Rémy-de-Provence, July 2026

> Generated from PRD.md.
> Every module listed here maps to a spec file in `architecture/modules/`.
> All PRD REQ-IDs are covered. No module exists outside the PRD scope.

---

## Overview

The app is a single static HTML file (`index.html`) deployed to GitHub Pages. There is no server, no build pipeline, and no npm. All dependencies are loaded from CDN at runtime. A Firebase Firestore database (free Spark tier) backs the Family Notes board — the only feature requiring a network connection after initial load.

The file is structured as a single-page application with five tabs. JavaScript manages tab switching and DOM visibility. Tailwind CSS handles all styling. Firebase JS SDK handles real-time Firestore reads and writes.

```
┌─────────────────────────────────────────────────────────┐
│                      index.html                         │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │               CDN Dependencies                  │   │
│  │  Tailwind CSS · Firebase App · Firebase Firestore│   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │                  App Shell                      │   │
│  │   router.js  ·  nav.js  ·  theme (CSS vars)     │   │
│  └──────┬──────┬──────┬──────┬──────┬──────────────┘   │
│         │      │      │      │      │                   │
│       Home  Trains  Stay  Guide  Notes                  │
│       tab    tab    tab   tab    tab                     │
│                                    │                    │
│                              ┌─────┴──────┐             │
│                              │  Firebase  │             │
│                              │  Firestore │             │
│                              └────────────┘             │
└─────────────────────────────────────────────────────────┘
                        │
              GitHub Pages (static hosting)
```

---

## Hosting

**GitHub Pages** serves `index.html` as a static file. No server-side logic. Deployment is a git push to the `gh-pages` branch (or `main` with Pages configured to root). The app is available at a single public URL shared with the family.

---

## CDN Dependencies

Loaded in `<head>` of `index.html`. No local copies. No npm.

| Dependency | Purpose | Load order |
|---|---|---|
| Tailwind CSS (Play CDN) | All styling and responsive layout | 1 |
| Firebase App (compat SDK) | Firebase initialization | 2 |
| Firebase Firestore (compat SDK) | Real-time notes database | 3 |

---

## Module Map

| Module | File | Implements |
|---|---|---|
| App Shell | `modules/app-shell.md` | REQ-1, REQ-1.1, REQ-1.2, REQ-1.3, REQ-8, REQ-9, REQ-10 |
| Home Tab | `modules/tab-home.md` | REQ-2, REQ-7 |
| Trains Tab | `modules/tab-trains.md` | REQ-3, REQ-3.1, REQ-3.2, REQ-3.3, REQ-3.4 |
| Stay Tab | `modules/tab-stay.md` | REQ-4, REQ-4.1, REQ-4.2, REQ-4.3 |
| Guide Tab | `modules/tab-guide.md` | REQ-5, REQ-5.1, REQ-5.2, REQ-5.3, REQ-5.4, REQ-5.5, REQ-5.6, REQ-5.7 |
| Notes Tab | `modules/tab-notes.md` | REQ-6, REQ-6.1, REQ-6.2 |

---

## Component Descriptions

### MOD-1: App Shell
**File:** `architecture/modules/app-shell.md`
**Implements:** REQ-1, REQ-1.1, REQ-1.2, REQ-1.3, REQ-8, REQ-9, REQ-10

The outer skeleton of `index.html`. Responsible for:
- HTML document structure and CDN `<script>`/`<link>` tags
- Tailwind configuration block (custom colors: terracotta, lavender, cream, olive)
- CSS custom properties for the Provençal color palette
- Bottom navigation bar (five tabs: Home, Trains, Stay, Guide, Notes)
- Tab router: shows/hides tab panels on nav click; sets active tab state
- Offline detection: listens to `window.online`/`offline` events; passes state to Notes tab
- Viewport meta tag ensuring correct mobile rendering on iOS Safari and Android Chrome

Tab panels are `<section>` elements with `id="tab-{name}"`. The router toggles `hidden` class. Only one panel is visible at a time.

**Connections:** Renders all five tab panels. Passes `isOnline` boolean to Notes module.

---

### MOD-2: Home Tab
**File:** `architecture/modules/tab-home.md`
**Implements:** REQ-2, REQ-7

A `<section id="tab-home">` panel containing:
- Trip title and dates header
- Traveler list (7 members, static HTML)
- Full trip timeline (8-row table, static HTML)
- House address block with one-tap Google Maps button
- Flights reference section (DL 220 outbound, DL 221 return; note about other travelers posting to Notes)

**Google Maps link:** `<a href="https://maps.google.com/?q=314+Chemin+de+Carraire+de+la+Crau,+13210+Saint-Rémy-de-Provence">` — opens native Maps app on mobile.

**Connections:** Static only. No JS logic beyond what the App Shell provides.

---

### MOD-3: Trains Tab
**File:** `architecture/modules/tab-trains.md`
**Implements:** REQ-3, REQ-3.1, REQ-3.2, REQ-3.3, REQ-3.4

A `<section id="tab-trains">` panel containing four journey cards, one per TGV booking. Each card displays:
- Journey header: train number, route, direction label
- Logistics row: departs / arrives / duration / class / coach / board-by time
- Seat table: traveler name | seat number | deck and position
- Transfer note (Avignon TGV → St. Rémy, 35–40 min, taxi)

Journey cards rendered top to bottom in chronological order:
1. Outbound Group 1 — Jul 4 (TGV 6109, Coach 8)
2. Outbound Group 2 — Jul 5 (TGV 6109, Coach 15)
3. Return Emmanuelle & Lukas — Jul 10 (TGV 6120, Coach 12)
4. Return Main Group — Jul 11 (TGV 6122, Coach 12)

Tables scroll horizontally within their container on narrow viewports (REQ-9).

**Connections:** Static only. No JS logic beyond App Shell tab routing.

---

### MOD-4: Stay Tab
**File:** `architecture/modules/tab-stay.md`
**Implements:** REQ-4, REQ-4.1, REQ-4.2, REQ-4.3

A `<section id="tab-stay">` panel containing three accommodation cards in trip order:

1. **Outbound Paris — Hotel Le Belmont** (Jul 3): address, metro, check-in/out dates, neighborhood, note about Alexandra and Colby's extra night.
2. **The House in St. Rémy** (Jul 5–11): address with one-tap Google Maps button (same link as REQ-2).
3. **Return Paris — Hotel TBD** (Jul 11): note explaining HotelTonight booking, train arrival time (6:22 PM), and that Olivier posts confirmed details to the Notes board.

**Connections:** Static only. Google Maps link identical to MOD-2.

---

### MOD-5: Guide Tab
**File:** `architecture/modules/tab-guide.md`
**Implements:** REQ-5, REQ-5.1–REQ-5.7

A `<section id="tab-guide">` panel with six sub-sections rendered as expandable or scrollable cards:

1. **Restaurants — Fine Dining** (REQ-5.1): L'Auberge de Saint-Rémy, Restaurant de Tourrel, Domaine de Baumanière.
2. **Restaurants — Casual** (REQ-5.2): Edú (with full address, phone, hours, closed days), Olga, Lou Patio, Canto Cigalo, Bienbon, Basta Cosi!
3. **Bakery** (REQ-5.3): Terre et Blé with address, phone, website, and go-early note.
4. **Saturday Market** (REQ-5.4): timing, what to find, practical tips.
5. **Things to Do** (REQ-5.5): eight attractions in two groups (Near / Day Trips) with drive times.
6. **FIFA World Cup 2026** (REQ-5.6): fan zones, local viewing, time-zone translation.
7. **Practical Tips** (REQ-5.7): weather, language, cash, rosé, driving, restaurant timing.

All content is static HTML. No JS required.

**Connections:** Static only. No JS logic beyond App Shell tab routing.

---

### MOD-6: Notes Tab
**File:** `architecture/modules/tab-notes.md`
**Implements:** REQ-6, REQ-6.1, REQ-6.2

A `<section id="tab-notes">` panel that is the only dynamic, network-dependent feature of the app.

**Structure:**
- Offline banner: shown when `isOnline === false` (passed from App Shell); hides form and feed, displays message
- Post form: Name field + Note textarea + Submit button
- Notes feed: reverse-chronological list of posted notes

**Firebase integration:**
- Firebase App and Firestore initialized once in `<script>` at bottom of `index.html`
- Firestore collection: `notes`
- Document fields: `name` (string), `text` (string), `timestamp` (Firestore `serverTimestamp()`)
- `onSnapshot` listener on the `notes` collection, ordered by `timestamp desc`, renders feed in real time
- On submit: validates both fields non-empty, calls `addDoc()`, clears form on success
- Security rules: anonymous read and write (no Firebase Auth)

**Firestore security rules (deployed separately via Firebase console or CLI):**
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /notes/{note} {
      allow read, write: if true;
    }
  }
}
```

**Connections:** Reads `isOnline` from App Shell. Depends on Firebase CDN scripts being loaded before this module initializes.

---

## Data Flow

```
User taps tab
    └── App Shell router
            └── hides all panels, shows selected panel

User posts a note (Notes tab, online)
    └── Form submit handler
            └── addDoc(notesCollection, { name, text, timestamp })
                    └── Firestore write
                            └── onSnapshot fires on all connected clients
                                    └── Feed re-renders with new note at top

Network goes offline
    └── window 'offline' event
            └── App Shell sets isOnline = false
                    └── Notes tab shows offline banner, disables form
```

---

## File Structure (Deployed)

```
france-trip/
├── index.html          ← entire app (all tabs inlined)
└── (no other files required)
```

All CSS is Tailwind utility classes. All JS is inline `<script>` blocks at the bottom of `index.html`. No separate `.js` or `.css` files needed.

---

## REQ Coverage Summary

| REQ | Module |
|-----|--------|
| REQ-1 | MOD-1 App Shell |
| REQ-1.1 | MOD-1 App Shell |
| REQ-1.2 | MOD-1 App Shell |
| REQ-1.3 | MOD-1 App Shell |
| REQ-2 | MOD-2 Home Tab |
| REQ-3 | MOD-3 Trains Tab |
| REQ-3.1 | MOD-3 Trains Tab |
| REQ-3.2 | MOD-3 Trains Tab |
| REQ-3.3 | MOD-3 Trains Tab |
| REQ-3.4 | MOD-3 Trains Tab |
| REQ-4 | MOD-4 Stay Tab |
| REQ-4.1 | MOD-4 Stay Tab |
| REQ-4.2 | MOD-4 Stay Tab |
| REQ-4.3 | MOD-4 Stay Tab |
| REQ-5 | MOD-5 Guide Tab |
| REQ-5.1 | MOD-5 Guide Tab |
| REQ-5.2 | MOD-5 Guide Tab |
| REQ-5.3 | MOD-5 Guide Tab |
| REQ-5.4 | MOD-5 Guide Tab |
| REQ-5.5 | MOD-5 Guide Tab |
| REQ-5.6 | MOD-5 Guide Tab |
| REQ-5.7 | MOD-5 Guide Tab |
| REQ-6 | MOD-6 Notes Tab |
| REQ-6.1 | MOD-6 Notes Tab |
| REQ-6.2 | MOD-6 Notes Tab |
| REQ-7 | MOD-2 Home Tab |
| REQ-8 | MOD-1 App Shell |
| REQ-9 | MOD-1 App Shell |
| REQ-10 | MOD-1 App Shell |
