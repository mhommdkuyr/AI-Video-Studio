# Repository Structure

## Purpose

This document defines the recommended monorepo structure for AI Video Studio. It establishes the organization of code, documentation, infrastructure, and tests so that future implementation work can scale across client, backend, AI, media processing, and platform operations.

The structure is intended to support enterprise-grade collaboration without over-fragmenting the platform into disconnected codebases.

## Monorepo Organization

The repository should be organized around the following top-level areas:

- apps/: end-user client experiences
- services/: backend and media processing services
- packages/: shared domain, contracts, and reusable platform components
- infrastructure/: deployment, containers, and environment configuration
- docs/: architecture, product, and engineering documentation
- tests/: cross-cutting test suites and validation assets

---

## apps/

The apps directory contains client-facing applications.

### mobile/

The mobile application is the primary end-user experience for creators and editors. It should host the Flutter-based application and its feature modules.

### web/

The web application layer may be introduced where a browser-based companion experience is required. It should share platform contracts and domain logic with the mobile application where practical.

### Responsibilities

- user interaction and experience delivery
- presentation and workflow orchestration
- integration with backend APIs and AI services
- local state and media handling
- cross-platform experience consistency

---

## services/

The services directory contains backend and platform services that provide the operational core of the system.

### backend/

The backend service layer should contain services for identity, projects, collaboration, workflows, and core platform operations.

### ai-core/

The AI services layer should contain the orchestration, agent coordination, command handling, provider abstraction, and tool execution logic.

### media-processing/

The media processing layer should contain services responsible for ingestion, metadata, asset preparation, rendering, export, and media operations.

### Responsibilities

- business operations and workflow execution
- service-to-service communication
- AI orchestration and tool execution
- media asset lifecycle and rendering workflows
- platform integrations and long-running processing

---

## packages/

The packages directory contains reusable shared assets that must be consumed across multiple applications and services.

### shared/

The shared package should contain common domain models, data structures, validation rules, and platform-wide utilities.

### api-contracts/

This package should hold shared API contract definitions, request/response schemas, and versioning information.

### design-system/

This package should define shared design language primitives, interaction conventions, and reusable platform experience assets where appropriate.

### common-utils/

This package should hold cross-cutting logic that is shared across clients and services, such as identifiers, serialization helpers, and policy logic where appropriate.

### Responsibilities

- shared abstractions and contracts
- reusable platform logic
- cross-team compatibility
- reduced duplication between client and service layers

---

## infrastructure/

The infrastructure directory contains deployment and environment definitions for the platform.

### Responsibilities

- container definitions
- deployment configuration
- cloud resource templates
- environment-specific configuration
- observability and monitoring setup
- security and access configuration

This directory should be treated as a first-class part of the product architecture, not as an afterthought.

---

## docs/

The docs directory stores all architecture, product, and engineering reference materials.

### Responsibilities

- system and solution architecture documentation
- product requirements and product strategy documentation
- engineering standards and implementation guidance
- operational and deployment documentation

The documentation should remain the source of truth for platform understanding and future implementation coordination.

---

## tests/

The tests directory should contain the test suites that validate the system across layers.

### Responsibilities

- unit tests for domain logic and shared utilities
- integration tests for service interactions and API behavior
- end-to-end tests for user flows and critical product scenarios
- performance and reliability validation assets

Testing should be treated as a shared engineering discipline across the repository, not as a separate concern owned by one team only.

---

## Directory Ownership Principles

Each directory should have a clear ownership and purpose:

- apps/: user experience delivery
- services/: platform and workflow execution
- packages/: shared contracts and reusable logic
- infrastructure/: environment and deployment definition
- docs/: architectural and product guidance
- tests/: verification and validation assets

This separation helps keep the codebase understandable as the product scales.

---

## Relationship to Existing Architecture

This repository structure is intended to align with the existing design documents:

- ARCHITECTURE.md for service decomposition
- AI_SYSTEM.md and AI_COMMAND_SPEC.md for AI orchestration placement
- API_CONTRACTS.md for shared interface organization
- FLUTTER_APPLICATION_ARCHITECTURE.md for client module organization
- BACKEND_SERVICES_DESIGN.md for service-level separation
