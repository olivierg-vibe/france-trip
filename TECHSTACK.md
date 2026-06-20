# Technology Stack

## Frontend
- Language: HTML, CSS, and JavaScript (vanilla — no framework)
- Styling: Tailwind CSS loaded via CDN (no build step, no npm)
- Single-page app with tab-based bottom navigation
- Mobile-first responsive design

## Database
- Firebase Firestore (free Spark tier) for the Family Notes board
- Anonymous read and write access (no login required)
- Firebase JavaScript SDK loaded via CDN
- Real-time sync across all family members' devices

## Hosting
- GitHub Pages (free static hosting)
- App accessible via a single public URL shared with the family

## Constraints
- No server, no backend, no build pipeline required
- All dependencies loaded via CDN — no npm, no node_modules
- Must work on iOS Safari and Android Chrome
- Static content (trains, hotels, guide) readable without internet
- Notes board requires an internet connection to post and sync
- App opens directly to content — no login screen, no onboarding
