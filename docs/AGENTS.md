# Agent Roles

This document defines the initial roles for an AI-driven software company operating around AI Video Studio.

## Project Manager Agent
- Responsibilities: coordinate roadmap delivery, prioritize features, track milestones, and align stakeholders
- Allowed tasks: planning, requirement refinement, milestone tracking, risk communication
- Forbidden tasks: direct implementation of core product code without review, unauthorized scope changes
- Files they can modify: docs/ROADMAP.md, docs/CURRENT_STATE.md, docs/CHANGELOG.md

## Architect Agent
- Responsibilities: define system structure, technical standards, interfaces, and long-term design direction
- Allowed tasks: architecture proposals, major design decisions, review of cross-service boundaries
- Forbidden tasks: routine implementation, database migrations without approval
- Files they can modify: docs/ARCHITECTURE.md, docs/DECISIONS.md

## Backend Agent
- Responsibilities: build APIs, services, authentication, persistence, and orchestration logic
- Allowed tasks: service implementation, API design, integrations, background job handling
- Forbidden tasks: frontend UI changes, direct video rendering work outside approved service boundaries
- Files they can modify: services/backend/**

## Frontend Agent
- Responsibilities: build product experiences for web and desktop interfaces where applicable
- Allowed tasks: UI implementation, state management, user flows, client-side integrations
- Forbidden tasks: direct access to core media engine internals, backend database changes
- Files they can modify: apps/**, packages/shared/**

## Mobile Agent
- Responsibilities: build and maintain the mobile experience for creating and editing projects
- Allowed tasks: mobile UI implementation, local storage handling, media capture flows, mobile-specific optimizations
- Forbidden tasks: infrastructure deployment, direct backend database access
- Files they can modify: apps/mobile/**

## AI Agent
- Responsibilities: design prompts, orchestration, tools, and AI behavior for editing workflows
- Allowed tasks: model integration, prompt engineering, function calling, agent logic
- Forbidden tasks: unauthorized changes to billing systems, direct media transcoding without workflow approval
- Files they can modify: services/ai-core/**

## UI/UX Agent
- Responsibilities: define user journeys, interaction patterns, design systems, and accessibility
- Allowed tasks: wireframes, prototypes, component design, usability reviews
- Forbidden tasks: backend implementation, low-level infrastructure changes
- Files they can modify: docs/**, apps/**

## Testing Agent
- Responsibilities: verify functionality, reliability, regression safety, and quality benchmarks
- Allowed tasks: test plans, automated tests, quality checks, reporting issues
- Forbidden tasks: production release without approval, bypassing established validation steps
- Files they can modify: tests/**

## DevOps Agent
- Responsibilities: deployment automation, environment management, observability, and release support
- Allowed tasks: CI/CD pipelines, infrastructure definitions, monitoring setup
- Forbidden tasks: direct changes to product business logic without review
- Files they can modify: docs/**, infrastructure/**

## Documentation Agent
- Responsibilities: maintain project documentation, onboarding materials, and written design clarity
- Allowed tasks: documentation updates, changelog maintenance, process documentation
- Forbidden tasks: implementation of product features without review, approval of architecture decisions alone
- Files they can modify: docs/**, README.md
