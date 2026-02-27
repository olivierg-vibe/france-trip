---
paths:
  - "poc/**/*"
---

# POC Mode Rules

## Detection
POC mode is active when the invoking command passes:
- `Module ID: POC-M{N}` (module IDs prefixed with `POC-`)
- `Coverage Target: 0%`

## Implementation Rules

1. **Mock everything:** No real APIs, databases, or auth. All data comes from mock files
2. **UI-focused:** No real backend server. Direct imports from mock data files. (For backend-focused projects, use mock API endpoints instead.)
3. **Navigation:** Every screen must be reachable by clicking through the UI
4. **No real integrations:** Dependencies are mocked, not connected to live services
5. **Standard quality rules still apply:** No scope creep, KISS, clean code

## Workflow Overrides
In POC mode, the standard implementation workflow is modified:

- **Skip integration sanity check:** No real dependencies to verify
- **Skip test readiness:** No unit tests or test fixtures required
- **Only gate:** Smoke test (app starts and screens render)

For test gate details, see `test-gates.md` (POC Mode Gates).
For test limit details, see `test-limits.md` (POC Mode).
For output locations and folder structure, see `project-structure.md` (poc/ section).
