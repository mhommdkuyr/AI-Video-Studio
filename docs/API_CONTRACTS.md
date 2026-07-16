# API Contracts

## Overview

This document defines the architectural contract for APIs across the AI Video Studio platform. It establishes how clients, services, and external integrations communicate with each other in a consistent, versioned, and secure manner.

The goal is to provide a stable contract layer that supports the mobile application, internal services, AI workflows, rendering pipelines, collaboration features, and future external developer APIs.

## API Design Principles

- Contract-first design: interfaces should be explicitly defined and versioned
- Provider-neutral communication: internal services should not depend on a single implementation detail
- Stable identifiers: resources should be addressable through durable IDs and clear resource ownership
- Explicit error semantics: failures should be categorized and actionable
- Auditability: every major request should be traceable
- Security by default: authentication and authorization should be enforced at the contract boundary

---

## API Architecture Layers

### Client APIs

Used by the Flutter application and other front-end experiences. These APIs support:

- authentication and session lifecycle
- project and timeline operations
- media import and retrieval
- AI command submission and status tracking
- render and export workflows
- collaboration and notifications

### Internal Service APIs

Used between backend services such as:

- project to media service communication
- AI orchestration to rendering service communication
- notification to user service communication
- billing to access policy evaluation

### External Developer APIs

Used by partner applications and API platform consumers. These should expose a limited, governed subset of core capabilities such as:

- project creation
- media import and export status
- AI command submission
- collaboration and publish workflows

---

## Versioning Strategy

The API layer should support explicit versioning to preserve compatibility as the platform evolves.

### Versioning Principles

- Use versioned resource paths or media types for major changes
- Preserve backward compatibility wherever possible
- Introduce additive changes before breaking changes
- Deprecate old versions with clear timelines
- Maintain compatibility information for clients and partners

### Compatibility Expectations

- Mobile clients should be able to operate against supported API versions without unexpected breakage
- Enterprise integrations should receive clear migration guidance for major changes
- AI command schemas and tool contracts should evolve separately from transport versioning where appropriate

---

## Authentication and Authorization

### Authentication Flow

The platform should use a standard authenticated session model for user-facing APIs and service-to-service tokens for internal operations.

### Authorization Model

Access should be evaluated based on:

- user identity
- workspace or tenant context
- project permissions
- feature entitlements
- policy rules for sensitive operations

### Sensitive Operations

Operations such as export, destructive edits, billing-related actions, AI generation with external services, and admin-level changes should require explicit approval or elevated privileges.

---

## Request and Response Standards

### Common Request Envelope

Requests should include standard metadata where appropriate:

- request ID
- correlation ID
- actor identity
- timestamp
- tenant or workspace context
- request version

### Common Response Envelope

Responses should include:

- request status
- resource state
- relevant metadata
- trace or correlation information
- structured errors where applicable

### Resource Representation

Resource responses should be normalized and consistently shaped so that clients can understand state, versions, permissions, and related resources without needing custom logic for each endpoint.

---

## Error Handling

Errors should be classified and returned in a structured form.

### Error Categories

- validation errors
- authentication failures
- authorization failures
- resource not found
- conflict or concurrency errors
- dependency or downstream service failures
- rate limiting or quota violations

### Error Response Requirements

Each error response should include:

- code
- message
- severity
- retry guidance where applicable
- correlation or request trace information

---

## Project APIs

Project APIs should manage the core lifecycle of editing work.

### Core Capabilities

- create or open project
- retrieve project metadata
- update project state
- list timeline and assets
- manage collaboration membership
- retrieve revision history

### Design Expectations

These endpoints should preserve project integrity and should support optimistic concurrency where appropriate.

---

## Timeline and Editing APIs

Timeline APIs should support the editorial workflow state required by the application.

### Core Capabilities

- read timeline structure
- apply edit operations
- update track and clip metadata
- request preview state
- manage undo and version state

These APIs should align with the editing model defined in the editor operations and video engine specifications.

---

## Media APIs

Media APIs should support asset ingestion, retrieval, and processing state.

### Core Capabilities

- upload media assets
- query asset metadata
- retrieve thumbnails or proxies
- trigger analysis or processing
- track processing status
- export asset references

These APIs should support both interactive use and background processing workflows.

---

## AI Command APIs

AI command APIs are a critical contract layer for the platform.

### Command Submission

Clients should submit AI requests as structured command payloads that include:

- command identity
- context and actors
- target assets
- requested operations
- parameters and constraints
- approval expectations
- execution preferences

### Command Execution Response

Responses should describe:

- accepted state
- queued or executing state
- preview availability
- completion status
- error details and rollback state where relevant

These APIs should align with AI_COMMAND_SPEC.md and AGENT_PROTOCOL.md.

---

## Rendering and Export APIs

Rendering APIs should manage the workflow from project state to output generation.

### Core Capabilities

- submit render job
- retrieve render status
- retrieve render artifacts or output references
- cancel or retry jobs
- list export history

These APIs should support background-based execution and asynchronous completion.

---

## Upload and Download APIs

The platform should expose APIs that support large media transfers and content delivery patterns.

### Upload Design Expectations

- resumable transfers where appropriate
- chunked or multipart support for large files
- progress reporting
- validation and integrity checks
- public or signed access for secure delivery

### Download Design Expectations

- signed retrieval or scoped access
- support for proxies, exports, and preview assets
- efficient access for mobile and web clients

---

## WebSocket and Real-Time Events

Real-time communication should support collaboration and workflow progress updates.

### Event Types

- project state change
- collaborator presence or activity
- AI command status updates
- render progress updates
- notification delivery
- sync conflict or resolution events

### Event Contract Principles

- event payloads should be versioned and stable
- events should carry correlation identifiers
- events should support replay or recovery where appropriate

---

## Relationship to Existing Architecture

This document should be read alongside:

- AI_COMMAND_SPEC.md for structured command contracts
- AGENT_PROTOCOL.md for AI activity coordination
- TOOL_SCHEMA.md for tool capability contracts
- ARCHITECTURE.md for service-system boundaries
- VIDEO_ENGINE_SPECIFICATION.md for execution-oriented operations and outputs
