# MOD-6: Notes Tab

## Requirement Coverage

| REQ ID | Requirement | Implementation |
|--------|-------------|----------------|
| REQ-6 | Append-only real-time shared notes board; no login; newest first | `<section id="tab-notes">` with Firestore `onSnapshot` feed |
| REQ-6.1 | Post a note: name + message fields; both required; form clears on submit | HTML form with validation; `addDoc()` on submit |
| REQ-6.2 | Firebase Firestore via CDN SDK; anonymous read/write; real-time `onSnapshot` | Firebase compat SDK loaded from CDN; no auth required |

---

## Responsibility

The only dynamic, network-dependent module in the app. Renders the Notes tab panel and manages all Firestore interaction: initializing Firebase, listening to the `notes` collection in real time, posting new notes, and handling the offline state passed from the App Shell.

---

## Panel Structure

```
<section id="tab-notes">
  ├── Section Header
  ├── Offline Banner         ← visible only when isOnline === false
  ├── Post Form              ← visible only when isOnline === true
  │     ├── Name field
  │     ├── Note textarea
  │     └── Submit button
  └── Notes Feed             ← reverse-chronological list of notes
        └── Note Card (×N)
              ├── Author name + timestamp
              └── Note text
</section>
```

---

## HTML Structure

```html
<section id="tab-notes" class="tab-panel px-4 py-6 hidden">
  <h2 class="text-xl font-bold text-terracotta mb-1">Family Notes</h2>
  <p class="text-sm text-gray-500 mb-4">Post a tip, a find, or anything worth sharing.</p>

  <!-- Offline Banner (hidden by default, shown when offline) -->
  <div id="notes-offline-banner"
       class="hidden bg-yellow-50 border border-yellow-200 rounded-xl px-4 py-3 mb-4 text-sm text-yellow-800">
    You're offline. Notes will appear once you reconnect.
  </div>

  <!-- Post Form -->
  <form id="notes-form" class="bg-white rounded-xl shadow-sm p-4 mb-6">
    <div class="mb-3">
      <label class="text-xs font-semibold text-gray-500 uppercase tracking-wide block mb-1"
             for="note-name">Your Name</label>
      <input id="note-name" type="text" required
             placeholder="e.g. Emmanuelle"
             class="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-terracotta">
    </div>
    <div class="mb-3">
      <label class="text-xs font-semibold text-gray-500 uppercase tracking-wide block mb-1"
             for="note-text">Note</label>
      <textarea id="note-text" required rows="3"
                placeholder="Great wine bar on the square in Arles..."
                class="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-terracotta resize-none"></textarea>
    </div>
    <button type="submit"
            class="w-full bg-terracotta text-white font-semibold py-2 rounded-lg text-sm">
      Post Note
    </button>
  </form>

  <!-- Notes Feed -->
  <div id="notes-feed" class="space-y-3">
    <!-- Populated by onSnapshot listener -->
  </div>
</section>
```

---

## Firebase Initialization

Firebase is initialized once, in the `<script>` block at the bottom of `index.html`, after the Firebase CDN scripts are loaded.

```javascript
const firebaseConfig = {
  apiKey:            "REPLACE_WITH_API_KEY",
  authDomain:        "REPLACE_WITH_AUTH_DOMAIN",
  projectId:         "REPLACE_WITH_PROJECT_ID",
  storageBucket:     "REPLACE_WITH_STORAGE_BUCKET",
  messagingSenderId: "REPLACE_WITH_MESSAGING_SENDER_ID",
  appId:             "REPLACE_WITH_APP_ID"
};

firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();
const notesCollection = db.collection('notes');
```

Firebase config values are taken from the Firebase console (Project Settings → General → Your apps). They are safe to include in client-side code for a public app — Firestore security rules control actual access, not the config keys.

---

## Real-Time Feed (onSnapshot)

```javascript
notesCollection
  .orderBy('timestamp', 'desc')
  .onSnapshot(snapshot => {
    const feed = document.getElementById('notes-feed');
    feed.innerHTML = '';
    snapshot.forEach(doc => {
      const { name, text, timestamp } = doc.data();
      const date = timestamp ? timestamp.toDate().toLocaleDateString('en-FR', {
        month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
      }) : '';
      const card = document.createElement('div');
      card.className = 'bg-white rounded-xl shadow-sm p-4';
      card.innerHTML = `
        <div class="flex justify-between items-baseline mb-1">
          <span class="font-semibold text-sm text-terracotta">${escapeHtml(name)}</span>
          <span class="text-xs text-gray-400">${date}</span>
        </div>
        <p class="text-sm text-gray-700 whitespace-pre-wrap">${escapeHtml(text)}</p>
      `;
      feed.appendChild(card);
    });
  });
```

`escapeHtml` sanitizes user-supplied content before inserting into the DOM to prevent XSS:

```javascript
function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
```

---

## Post Form Handler

```javascript
document.getElementById('notes-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const nameInput = document.getElementById('note-name');
  const textInput = document.getElementById('note-text');

  const name = nameInput.value.trim();
  const text = textInput.value.trim();

  if (!name || !text) return; // HTML `required` handles UI; this is the JS guard

  try {
    await notesCollection.addDoc({
      name,
      text,
      timestamp: firebase.firestore.FieldValue.serverTimestamp()
    });
    nameInput.value = '';
    textInput.value = '';
  } catch (err) {
    console.error('Failed to post note:', err);
    // Surface a brief inline error message to the user
    alert('Could not post note. Check your connection and try again.');
  }
});
```

`serverTimestamp()` is used (not `new Date()`) so ordering is consistent regardless of client clock differences.

---

## Offline State Handling

The App Shell dispatches an `onlineStateChange` CustomEvent whenever the network state changes. The Notes module listens and toggles UI accordingly.

```javascript
document.addEventListener('onlineStateChange', (e) => {
  const online = e.detail.online;
  document.getElementById('notes-offline-banner').classList.toggle('hidden', online);
  document.getElementById('notes-form').classList.toggle('hidden', !online);
});
```

When offline:
- The post form is hidden
- The offline banner is shown
- The feed may still show cached Firestore data (Firestore JS SDK caches locally)

When reconnected:
- The post form reappears
- The offline banner hides
- `onSnapshot` delivers any notes posted while offline

---

## Firestore Data Model

**Collection:** `notes`

**Document fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Author name as entered (not sanitized in DB; sanitized on render) |
| `text` | string | Note body |
| `timestamp` | Timestamp | Server-generated via `FieldValue.serverTimestamp()` |

**No document ID constraints** — Firestore auto-generates IDs via `addDoc()`.

**No delete or update operations** — append-only by design. No UI for editing or removing notes.

---

## Firestore Security Rules

Deployed via the Firebase console or Firebase CLI. Allows anonymous read and write on the `notes` collection only.

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

These rules are intentionally permissive — this is a private family app shared by URL, not a public product. No authentication is required.

---

## Inputs

| Input | Source |
|-------|--------|
| `<section id="tab-notes">` mount point | MOD-1 App Shell |
| `onlineStateChange` CustomEvent | MOD-1 App Shell |
| Firebase App and Firestore CDN scripts (loaded before this module's `<script>`) | MOD-1 App Shell |
| Tailwind color classes | MOD-1 App Shell |

---

## Outputs

None. This module produces no outputs consumed by other modules.

---

## Dependencies

| Dependency | Module / Service |
|------------|-----------------|
| Tab panel mount point and routing | MOD-1 App Shell |
| `onlineStateChange` CustomEvent | MOD-1 App Shell |
| Firebase CDN scripts | MOD-1 App Shell (loaded in `<head>`) |
| Firestore database | Firebase (external — free Spark tier) |

---

## Notes

- `serverTimestamp()` must be used for the `timestamp` field — client timestamps are unreliable for ordering across devices in different time zones.
- All user-supplied content (`name`, `text`) must be HTML-escaped before `innerHTML` insertion. The `escapeHtml` helper is defined once and reused.
- The Firestore security rules are stored and deployed separately from `index.html` (via Firebase console). They are documented here for traceability but are not part of the HTML artifact.
- Firebase config values (`apiKey`, `projectId`, etc.) are client-facing by design in Firebase's architecture. They do not grant admin access — Firestore security rules are the enforcement layer.
- The `addDoc` compat API is used (not `setDoc`) so document IDs are auto-generated and never collide.
