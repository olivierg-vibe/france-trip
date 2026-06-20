# Product Requirements Document
## France Family Trip App — St. Rémy-de-Provence, July 2026

> Generated from OVERVIEW.md and TECHSTACK.md.
> REQ-IDs are permanent — do not renumber.

---

## REQ-1: Application Shell

The system shall be a single-page application delivered as a static HTML file, hosted on GitHub Pages, accessible via a single public URL with no login, no build step, and no server.

**Acceptance Criteria:**
- App loads in a single browser request (one HTML file, CDN assets only)
- No authentication screen — content is visible immediately on load
- Works on iOS Safari and Android Chrome
- URL is shareable; anyone with the link can open the app

### REQ-1.1: Bottom Navigation

The app shall display a persistent bottom navigation bar with five tabs: Home, Trains, Stay, Guide, Notes.

**Acceptance Criteria:**
- Navigation bar is fixed to the bottom of the viewport on all screen sizes
- Active tab is visually highlighted
- Switching tabs shows the corresponding section without a page reload
- Tab labels and icons are legible on small mobile screens

### REQ-1.2: Visual Design

The app shall use a Provençal color palette (terracotta, lavender, cream, olive) with mobile-first responsive layout via Tailwind CSS loaded from CDN.

**Acceptance Criteria:**
- Tailwind CSS loaded via CDN — no npm, no build pipeline
- Color palette applied consistently across all tabs
- Layout renders correctly at 375px viewport width and above
- Text is readable without zooming on a standard mobile screen

### REQ-1.3: Offline Static Content

All static content (Trains, Stay, Guide tabs) shall be readable without an internet connection after the initial page load.

**Acceptance Criteria:**
- Trains, Stay, and Guide tabs render fully with no network requests after first load
- Notes tab gracefully indicates when offline (post/sync disabled, read unavailable)

---

## REQ-2: Home Tab

The Home tab shall display a trip overview: the traveler list, the full trip timeline, and a one-tap link to open the house address in Google Maps.

**Acceptance Criteria:**
- Traveler list shows all seven family members
- Timeline table shows all eight date/event rows from OVERVIEW.md
- House address (314 Chemin de Carraire de la Crau, 13210 Saint-Rémy-de-Provence) is displayed prominently
- A single tap on the address opens Google Maps to that location (via `maps.google.com/?q=` or `geo:` URI)

---

## REQ-3: Trains Tab

The Trains tab shall display all four TGV journeys with complete booking details, grouped by journey, so any traveler can find their seat number in under five seconds.

**Acceptance Criteria:**
- Four journeys displayed: Outbound Group 1 (Jul 4), Outbound Group 2 (Jul 5), Return Emmanuelle & Lukas (Jul 10), Return Main Group (Jul 11)
- Each journey shows: train number, route, departure time, arrival time, duration, class, coach, board-by time
- Each journey shows a per-traveler seat table (traveler name, seat number, deck/position)
- Transfer note is displayed: "Avignon TGV is outside the city center — allow 35–40 min by taxi"

### REQ-3.1: Outbound — Group 1 (July 4)

TGV INOUI 6109, Paris Gare de Lyon → Avignon TGV, departs 10:38 AM, arrives 1:19 PM, 2nd Class, Coach 8.

| Traveler          | Seat | Position             |
|-------------------|------|----------------------|
| Olivier Gers      | 813  | Lower deck, Window   |
| Dana Gers         | 806  | Lower deck, Corridor |
| Emmanuelle Gers   | 807  | Lower deck, Window   |
| Lukas Stachtiaris | 812  | Lower deck, Corridor |

### REQ-3.2: Outbound — Group 2 (July 5)

TGV INOUI 6109, Paris Gare de Lyon → Avignon TGV, departs 10:38 AM, arrives 1:19 PM, 2nd Class, Coach 15.

| Traveler       | Seat | Position             |
|----------------|------|----------------------|
| Alexandra Gers | 559  | Upper deck, Window   |
| Colby Gates    | 558  | Upper deck, Corridor |

### REQ-3.3: Return — Emmanuelle & Lukas (July 10)

TGV INOUI 6120, Avignon TGV → Paris Gare de Lyon, departs 2:41 PM, arrives 5:22 PM, 1st Class, Coach 12.

| Traveler          | Seat | Position             |
|-------------------|------|----------------------|
| Emmanuelle Gers   | 272  | Upper deck, Window   |
| Lukas Stachtiaris | 271  | Upper deck, Corridor |

### REQ-3.4: Return — Main Group (July 11)

TGV INOUI 6122, Avignon TGV → Paris Gare de Lyon, departs 3:37 PM, arrives 6:22 PM, 1st Class, Coach 12.

| Traveler       | Seat | Position             |
|----------------|------|----------------------|
| Olivier Gers   | 244  | Upper deck, Corridor |
| Dana Gers      | 247  | Upper deck, Corridor |
| Alexandra Gers | 248  | Upper deck, Window   |
| Colby Gates    | 245  | Upper deck, Window   |

---

## REQ-4: Stay Tab

The Stay tab shall display all accommodation details for the trip: the outbound Paris hotel, the house in St. Rémy, and the return Paris hotel note.

**Acceptance Criteria:**
- Three sections rendered: Outbound Paris Night, The House, Return Paris Night
- Each section shows full address and relevant details
- House address includes one-tap Google Maps button (same as REQ-2)

### REQ-4.1: Outbound Paris Hotel (July 3)

Display Hotel Le Belmont Paris: address (30 Rue de Bassano, 75116 Paris), metro (George V, Line 1), check-in July 3 / check-out July 4, neighborhood note, and the note that Alexandra and Colby stay one additional night.

### REQ-4.2: The House in St. Rémy (July 5–11)

Display the house address: 314 Chemin de Carraire de la Crau, 13210 Saint-Rémy-de-Provence. Include a one-tap button to open in Google Maps.

### REQ-4.3: Return Paris Hotel (July 11)

Display a note that the hotel is TBD, will be booked via HotelTonight day-of or day-before, and that Olivier will post the confirmed name and address to the Family Notes board.

---

## REQ-5: Guide Tab

The Guide tab shall display the St. Rémy-de-Provence local guide, organized into sections: Restaurants, Bakery, Saturday Market, Things to Do, FIFA World Cup, and Practical Tips.

**Acceptance Criteria:**
- All six sections present and scannable on mobile
- Restaurant entries include name, tier (Fine Dining / Casual), and key details (address, phone, hours, closure days where specified)
- Things to Do entries include distance/drive time from St. Rémy
- World Cup section includes fan zone cities and timing guidance
- Practical Tips section covers weather, language, cash, wine, driving, and restaurant timing

### REQ-5.1: Restaurants — Fine Dining

Display three fine dining entries: L'Auberge de Saint-Rémy (Michelin, Chef Fanny Rey), Restaurant de Tourrel (Michelin, 17th-century mansion), Domaine de Baumanière (two Michelin stars, Les Baux-de-Provence, 20 min away).

**Acceptance Criteria:**
- Each entry notes Michelin star count and reservation urgency for July

### REQ-5.2: Restaurants — Casual and Local Favorites

Display six casual entries: Edú, Olga by le Bistrot Découverte, Restaurant Lou Patio, Bistrot Canto Cigalo, Bienbon, Basta Cosi!

**Acceptance Criteria:**
- Edú entry includes: address (17 Av. Albert Schweitzer), phone (+33 4 90 20 94 21), CLOSED Sunday and Monday, hours (lunch noon–1:30 PM, dinner 7–9 PM), and parking note
- TheFork ratings shown where available (Olga 8.9, Lou Patio 8.9, Canto Cigalo 8.6)

### REQ-5.3: Bakery

Display Terre et Blé: address (ZAC de la Gare, 24 Av. Albin Gilles), phone (+33 4 90 89 72 30), website (terredeble.com), and notes (sourdough, sells out early, open Mondays).

### REQ-5.4: Saturday Market

Display market information: location (Boulevard Mirabeau and surrounding streets), dates the family will attend (July 5 and July 11), arrival timing advice (8:30–9 AM for bread, 10–11 AM for full market), what to find, and practical tips (cash, park outside).

### REQ-5.5: Things to Do

Display eight attractions in two groups:

Near St. Rémy (under 30 min): Les Baux-de-Provence, Saint-Paul-de-Mausole, Glanum (Les Antiques), Les Alpilles Natural Park.

Day Trips (30–60 min): Arles (35 min), Avignon (25 min), Luberon (Gordes/Roussillon/Bonnieux), Camargue (45 min).

**Acceptance Criteria:**
- Each entry includes drive time and a one-line description
- Crowd/timing tips shown where specified (Les Baux before 10 AM, Camargue early morning)

### REQ-5.6: FIFA World Cup 2026

Display World Cup viewing information covering the family's stay (July 4–11, Round of 16 and Quarterfinals).

**Acceptance Criteria:**
- Fan zone cities listed with drive times: Avignon (25 min), Aix-en-Provence (40 min), Arles (35 min)
- St. Rémy local viewing note (Place de la République cafés and bars)
- Time zone translation note (3 PM ET = 9 PM local)
- Reminder to check France's bracket position before departure

### REQ-5.7: Practical Tips

Display tips covering: weather (30–35°C, siesta hours), language (French, Bonjour), cash, rosé wine estates (Hauvette, Trévallon, Romanin), driving (narrow streets, roundabouts), and restaurant timing (dinner after 7:30 PM, lunch ends 1:30 PM).

---

## REQ-6: Notes Tab — Family Notes Board

The Notes tab shall implement an append-only, real-time shared notes board backed by Firebase Firestore, requiring no login, where any family member can post a note that appears instantly on all other devices.

**Acceptance Criteria:**
- Notes board loads and displays existing notes without login
- Newest notes appear at the top (reverse chronological)
- No editing or deleting of posted notes
- Notes require an internet connection; tab shows a clear offline state when disconnected
- Real-time sync: a note posted on one device appears on another within a few seconds without page refresh

### REQ-6.1: Post a Note

Any user shall be able to post a note by entering their name and a message, then tapping a submit button.

**Acceptance Criteria:**
- Form has two fields: Name and Note text
- Both fields required; submit is blocked if either is empty
- On submit, note is written to Firestore and appears at the top of the list immediately
- Form clears after successful submission
- Name field is not pre-filled or persisted (no local storage requirement)

### REQ-6.2: Firebase Firestore Integration

The Notes board shall use Firebase Firestore (free Spark tier) with anonymous read and write access, using the Firebase JavaScript SDK loaded from CDN.

**Acceptance Criteria:**
- Firebase SDK loaded via CDN — no npm, no build step
- Firestore security rules allow anonymous read and write
- Real-time listener (`onSnapshot`) used so new notes appear without polling
- No Firebase Authentication required

---

## REQ-7: Flights Reference

The app shall display the confirmed flight details for Olivier and Dana as reference information, accessible from the Home or Stay tab (not a dedicated tab).

**Acceptance Criteria:**
- Outbound: DL 220, SLC → CDG, departs ~3:25 PM MDT July 2, arrives ~9:30 AM CEST July 3, Terminal 2E, A330-300
- Return: DL 221, CDG → SLC, July 12 (departure time TBC from booking confirmation)
- Note displayed that other travelers have separate arrangements and will post details to the Notes board

---

## Non-Functional Requirements

### REQ-8: Performance

**Acceptance Criteria:**
- App reaches interactive state within 3 seconds on a 4G mobile connection
- Static tabs (Home, Trains, Stay, Guide) render with zero network requests after initial load
- No JavaScript framework or bundler — vanilla JS only

### REQ-9: Compatibility

**Acceptance Criteria:**
- Full functionality on iOS Safari 16+ and Android Chrome 110+
- Layout does not break or require horizontal scrolling on 375px viewport
- Tables (train seats, traveler lists) scroll horizontally within their container if needed on narrow screens

### REQ-10: Reliability and Hosting

**Acceptance Criteria:**
- Hosted on GitHub Pages — no server to maintain
- Static content available even if Firebase is unreachable
- Single deployable artifact: one HTML file (plus any inlined assets)
