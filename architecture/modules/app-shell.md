# MOD-1: App Shell

## Requirement Coverage

| REQ ID | Requirement | Implementation |
|--------|-------------|----------------|
| REQ-1 | Single static HTML file, no login, no server | `index.html` is the entire app; no backend; GitHub Pages hosting |
| REQ-1.1 | Bottom navigation bar with five tabs | Fixed `<nav>` at viewport bottom; JS router shows/hides panels |
| REQ-1.2 | Provençal color palette, Tailwind CDN, mobile-first | Tailwind Play CDN; custom color config block; viewport meta tag |
| REQ-1.3 | Static content readable offline after first load | Tab panels are static HTML; only Notes tab makes network calls |
| REQ-8 | Interactive within 3 seconds on 4G; vanilla JS only | No framework; CDN scripts are the only external requests |
| REQ-9 | iOS Safari 16+ and Android Chrome 110+; 375px min width | Viewport meta; no CSS features requiring newer support |
| REQ-10 | GitHub Pages hosting; single deployable artifact | `index.html` only; no build output directory needed |

---

## Responsibility

The App Shell is the outer document — `index.html` — that every other module lives inside. It owns:

1. The HTML document structure (`<head>`, `<body>`)
2. All CDN `<script>` and `<link>` tags
3. Tailwind custom theme configuration
4. The bottom navigation bar
5. The tab routing logic
6. Online/offline state detection and propagation

It does not own the content of any tab. Tab panels are rendered by their respective modules (MOD-2 through MOD-6) as `<section>` elements inside the body.

---

## HTML Document Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>France Trip — July 2026</title>

  <!-- CDN: Tailwind Play CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Tailwind custom theme config -->
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            terracotta: '#C0674A',
            lavender:   '#8B7BA8',
            cream:      '#F5F0E8',
            olive:      '#6B7B3A',
          }
        }
      }
    }
  </script>

  <!-- CSS custom properties (used by nav active states and global accents) -->
  <style>
    :root {
      --color-terracotta: #C0674A;
      --color-lavender:   #8B7BA8;
      --color-cream:      #F5F0E8;
      --color-olive:      #6B7B3A;
    }
    body { background-color: #F5F0E8; }
    /* Prevent horizontal scroll on narrow viewports */
    body { overflow-x: hidden; }
    /* Scrollable table containers */
    .table-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
  </style>
</head>
<body class="font-sans text-gray-800 pb-16">

  <!-- Tab Panels (MOD-2 through MOD-6 render their content here) -->
  <section id="tab-home"   class="tab-panel px-4 py-6"> ... </section>
  <section id="tab-trains" class="tab-panel px-4 py-6 hidden"> ... </section>
  <section id="tab-stay"   class="tab-panel px-4 py-6 hidden"> ... </section>
  <section id="tab-guide"  class="tab-panel px-4 py-6 hidden"> ... </section>
  <section id="tab-notes"  class="tab-panel px-4 py-6 hidden"> ... </section>

  <!-- Bottom Navigation Bar -->
  <nav id="bottom-nav" class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 flex z-50">
    <button data-tab="home"   class="nav-btn flex-1 ...">🏠<span>Home</span></button>
    <button data-tab="trains" class="nav-btn flex-1 ...">🚄<span>Trains</span></button>
    <button data-tab="stay"   class="nav-btn flex-1 ...">🏡<span>Stay</span></button>
    <button data-tab="guide"  class="nav-btn flex-1 ...">🗺️<span>Guide</span></button>
    <button data-tab="notes"  class="nav-btn flex-1 ...">📝<span>Notes</span></button>
  </nav>

  <!-- Firebase SDK (loaded before Notes module script) -->
  <script src="https://www.gstatic.com/firebasejs/9.x.x/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.x.x/firebase-firestore-compat.js"></script>

  <!-- App Shell router + offline detection -->
  <script> /* see Router Logic section below */ </script>

  <!-- Notes Tab module script (MOD-6) -->
  <script> /* Firebase init + Firestore logic */ </script>

</body>
</html>
```

---

## Router Logic

```javascript
(function () {
  const panels = document.querySelectorAll('.tab-panel');
  const buttons = document.querySelectorAll('.nav-btn');

  function showTab(name) {
    panels.forEach(p => p.classList.toggle('hidden', p.id !== 'tab-' + name));
    buttons.forEach(b => {
      const active = b.dataset.tab === name;
      b.classList.toggle('text-terracotta', active);
      b.classList.toggle('text-gray-400', !active);
    });
  }

  buttons.forEach(b => b.addEventListener('click', () => showTab(b.dataset.tab)));

  // Default to Home on load
  showTab('home');
})();
```

---

## Offline Detection

```javascript
(function () {
  function setOnline(online) {
    document.dispatchEvent(new CustomEvent('onlineStateChange', { detail: { online } }));
  }
  window.addEventListener('online',  () => setOnline(true));
  window.addEventListener('offline', () => setOnline(false));
  // Emit initial state after DOM ready
  setOnline(navigator.onLine);
})();
```

MOD-6 (Notes Tab) listens for `onlineStateChange` to show/hide the offline banner and enable/disable the post form.

---

## Inputs

None. The App Shell is the root — it has no upstream dependencies.

---

## Outputs

| Output | Consumed by |
|--------|-------------|
| `<section id="tab-{name}">` mount points | MOD-2, MOD-3, MOD-4, MOD-5, MOD-6 |
| `onlineStateChange` CustomEvent | MOD-6 Notes Tab |
| Tailwind custom colors (`terracotta`, `lavender`, `cream`, `olive`) | All tab modules |
| Firebase CDN scripts loaded and available on `window` | MOD-6 Notes Tab |

---

## Dependencies

None. This module has no dependencies on other modules.

---

## Notes

- `pb-16` on `<body>` prevents content from being hidden behind the fixed nav bar
- Tab icons are emoji for zero-dependency iconography; replaceable with SVG if desired
- The `hidden` Tailwind class maps to `display: none` — no animation between tabs (by design; speed over polish on mobile)
- Firebase CDN scripts must appear before the MOD-6 `<script>` block
