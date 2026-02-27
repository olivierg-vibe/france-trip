## Hyperdrive - DCF Methodology

This project uses **DCF (Design Cascading Framework)** - a top-down approach where design cascades from requirements through architecture to implementation.


### The Flow

```
OVERVIEW.md (Requirements)
       ↓
PRD.md (Structured requirements with REQ-IDs)
       ↓
architecture.md (High-Level Design with Implements: tags)
       ↓
module-{N}-{name}.md (Low-Level Design with Requirement Coverage)
       ↓
Implementation Code (Generated from module specs)
       ↓
Deployed System
```

### Key Principle: Derivation, Not Invention

- **PRD.md** = WHAT the system must do (numbered requirements with REQ-IDs)
- **architecture.md** = WHAT the system is (high-level boxes, flows, integrations)
- **module specs** = HOW each piece works (pseudo-code, schemas, API contracts)
- **implementation** = The actual code following module specs

Modules are DERIVED from architecture, not invented. The Sum Test validates:
```
Module 1 + Module 2 + ... + Module N = architecture.md (exactly)
```

No feature invention. No scope expansion. Architecture is the single source of truth.

### Process (DCF Workflow Steps)
1. **Step 0**: Requirements → OVERVIEW.md
2. **Step 1**: PRD → /generate-prd creates PRD.md with REQ-IDs
3. **Step 2**: Architecture → /generate-architecture creates architecture.md
4. **Step 3**: Modules → /generate-modules extracts module specs
5. **Step 4**: Implementation → /generate-code with mandatory L1/L2 test gates
6. **Step 5**: Deployment → /deploy-module command

### POC Workflow (optional, before Step 4)
- /generate-poc → navigatable proof-of-concept with mock data (in `poc/`)
- /modify-poc → apply stakeholder feedback to the POC
- /sync-prd → merge validated POC changes back into PRD


## Key References

- Project overview @OVERVIEW.md
- Product Requirements Document (The formal requirements to be implemented) @PRD.md
- Technology Stack to be used in development @TECHSTACK.md
- Master architecture with Integration Matrix @architecture/architecture.md
- Module specs - COMPLETE implementation blueprint @architecture/modules/*
- SOURCE OF TRUTH for module development/completion status @tracking/*

## Core Rules

**Working Guidelines:**
- Do exactly what's asked; nothing more, nothing less

 **Simplicity (KISS):**
 - Simplest working solution wins
 - YAGNI - no hypothetical future features

 **Security (OWASP):**
 - Never hardcode secrets - use configuration options
 - Never concatenate SQL/commands - use parameterized APIs
 - Never log PII/passwords/tokens

 **Code Quality:**
 - Single Responsibility per module/class/function
 - Explicit names, no magic numbers
 - Fail fast, validate early
 - Immutable by default, pure functions preferred

 **Error Handling:**
 - Friendly user messages, detailed logs
 - Never swallow exceptions
 - Timeout all external calls