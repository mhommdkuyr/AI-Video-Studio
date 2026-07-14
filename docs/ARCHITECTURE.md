# Architecture

## Overview
AI Video Studio will use a modular, service-oriented architecture with clear separation between mobile experience, backend services, AI orchestration, and media processing.

## High-Level Components
- Mobile app: cross-platform client for creating and managing projects
- Backend: user accounts, projects, storage coordination, permissions, and APIs
- AI Core: natural language understanding, agent orchestration, tool use, and prompt management
- Video Engine: timeline rendering, transcoding, effects, and export processing
- Cloud Services: scalable storage, queues, background workers, and media processing infrastructure
- Shared Package: common contracts, schemas, and utilities used across services

## Communication Model
- The mobile app communicates with the backend over REST and WebSocket APIs
- The backend coordinates jobs and dispatches work to AI and video services
- AI agents receive structured tasks from the backend and use tools to perform actions
- The video engine processes media jobs asynchronously and reports status back to the backend
- Cloud services provide storage, queueing, and execution resources for heavy workloads
- Shared packages ensure consistent models, interfaces, and validation rules

## Deployment Principles
- Stateless backend services where possible
- Event-driven processing for long-running jobs
- Hybrid processing strategy: local for lightweight tasks, cloud for intensive ones
- Provider-agnostic AI integration with support for Gemini, DeepSeek, and Ollama
- Observability, tracing, and monitoring across services
