---
paths:
  - "src/**/*"
  - "tests/**/*"
---

# Test Gate Enforcement

All code changes must pass test gates before being considered complete.

## L1 Gate (Unit Tests)
- **Minimum 60% coverage** per module (default, configurable)
- **Maximum 5 tests** per module
- Run with the project's test runner (e.g., `npx vitest`, `pytest`, `go test`)
- Tests must be in `{name}.test.{ext}` format (e.g., `.ts`, `.py`, `.go`)
- CANNOT proceed to Smoke Test without passing L1

## Coverage Parameterization
The default coverage target is 60%. Invoking commands (e.g., /generate-code, /generate-poc)
pass the actual coverage target to agents. Agents use the value provided by the invoking command.

## Smoke Test Gate (BLOCKING)
- Application must start without crashing
- Basic functionality must respond
- BLOCKING - module cannot proceed if smoke fails
- **Apply smoke test** to modules that produce runnable code (backend servers, frontend apps)
- **Skip smoke test** for foundational modules (data models, utilities, shared libraries) with no runnable entry points
- Determine classification by reading the module spec and checking for runnable endpoints or rendered UI

## L2 Gate (Integration Tests)
- Cross-module validation for critical flows
- **Maximum 10 integration tests** total
- Tests must be in `integration.test.{ext}` format
- Run after all modules pass L1 + Smoke

## Code Review (OPTIONAL)
- Only runs with `-review` flag
- Skipped by default for speed
- Use when quality is more important than speed

## Enforcement
- After implementing code, ALWAYS run the relevant test suite
- Report coverage percentage
- If below 60% (default), add more tests before marking module complete
- Use `/update-tracking` to record test status

## Gate Summary

| Gate | Coverage/Tests | Blocking | When |
|------|----------------|----------|------|
| L1 Unit Tests | 60% min (default), 5 max | YES | After each module |
| Smoke Test | App runs | YES | After L1 (runnable modules) |
| Code Review | N/A | NO | Optional (-review) |
| L2 Integration | 10 max | YES | After all modules |
