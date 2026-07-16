# Development Guidelines

## Purpose

This document defines the engineering standards and collaboration rules that should govern future implementation work for AI Video Studio. It is intended to ensure consistency across the Flutter client, backend services, AI orchestration, media processing, and infrastructure work.

These guidelines are not implementation instructions for feature delivery; they define the operating model for how the codebase should be built, reviewed, documented, and maintained.

## Core Engineering Principles

- Build for clarity and maintainability over short-term convenience.
- Keep domain boundaries explicit and service responsibilities well-defined.
- Favor reusable contracts, shared models, and consistent interfaces.
- Preserve traceability for AI workflows, media jobs, approvals, and project changes.
- Treat security, observability, and testability as first-class engineering concerns.
- Prefer deterministic behavior for editing and execution workflows.

---

## Coding Standards

### General Standards

- Write code that is readable, modular, and easy to reason about.
- Keep functions and components focused on a single responsibility.
- Avoid hidden side effects and ambiguous state transitions.
- Use explicit error handling and structured failure propagation.
- Maintain a consistent level of abstraction within each module.

### Architecture Conformance

- Keep client code aligned with the Flutter application architecture.
- Keep service code aligned with the published backend service boundaries.
- Respect the command, agent, tool, and data contracts already defined in the architecture set.
- Avoid introducing direct cross-layer coupling that bypasses the intended architecture.

---

## Naming Conventions

### General Naming

- Use clear, descriptive names that reflect business meaning.
- Prefer domain language over implementation language where appropriate.
- Use consistent naming across services, modules, APIs, and data models.

### Suggested Conventions

- Feature modules should use concise, domain-oriented names.
- Files and classes should reflect the responsibility they own.
- API resources should use stable, predictable naming patterns.
- State objects should clearly represent their scope and lifecycle.

---

## Documentation Rules

- Every substantial module should have clear documentation at the architectural level.
- Public contracts, interfaces, and workflows should be documented where they affect other teams.
- Changes to business rules, data contracts, or workflows should be reflected in the relevant architecture documents.
- Documentation should be updated when behavior, contracts, or responsibilities change.

### Required Documentation Alignment

When adding or changing a feature, the implementation should remain aligned with:

- ARCHITECTURE.md
- AI_SYSTEM.md
- AI_COMMAND_SPEC.md
- AGENT_PROTOCOL.md
- TOOL_SCHEMA.md
- DATA_MODELS.md
- API_CONTRACTS.md
- FLUTTER_APPLICATION_ARCHITECTURE.md
- BACKEND_SERVICES_DESIGN.md

---

## Code Review Principles

Code review should focus on:

- correctness and correctness of intent
- architecture compliance
- readability and maintainability
- test coverage and test quality
- security and privacy considerations
- observability and operational concerns

Reviewers should look for:

- hidden coupling between layers
- duplicated logic that should be shared
- missing validation or error handling
- unclear ownership or responsibility boundaries
- unreviewed changes to contracts, schemas, or permissions

---

## Branch Strategy

A structured branch strategy should be used to keep work organized and safe.

### Recommended Branch Model

- main: stable integration branch
- feature/*: work for distinct product or platform capabilities
- fix/*: bug fixes and corrective changes
- chore/*: non-functional maintenance and documentation work
- release/*: release preparation branches where appropriate

### Branch Rules

- Branches should be short-lived where practical.
- Merge only after review, validation, and alignment with the architecture.
- Do not merge changes that are incomplete, untested, or not traceable to a documented requirement.

---

## Commit Conventions

Commits should be clear, atomic, and descriptive.

### Commit Principles

- One logical change per commit where possible
- Clear commit messages that explain the change and its intent
- Reference related tickets, tasks, or design documents when useful

### Example Commit Style

- feat: add AI command workflow contract
- fix: correct rendering job state handling
- docs: update backend service boundaries
- chore: align repository structure documentation

---

## Dependency Management Rules

Dependencies should be managed intentionally and conservatively.

### Rules

- Prefer shared packages and internal libraries over duplicate implementations.
- Keep dependencies aligned with the architecture and supported platform requirements.
- Review dependency scope, maintenance status, and security posture before adoption.
- Avoid unnecessary dependency sprawl across services and client modules.
- Keep versioning consistent wherever cross-project integration is expected.

---

## Change Management and Traceability

Every significant implementation change should preserve traceability to:

- the relevant product requirement
- the architecture decision or document
- the relevant API or data contract
- the corresponding test strategy and verification step

This ensures the platform remains understandable as it grows.
