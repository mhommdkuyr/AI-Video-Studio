# AI System

## Goal
The AI system will translate natural language instructions into structured editing operations that can be executed safely and predictably.

## Command Flow
1. User submits a request in natural language.
2. The AI layer interprets the intent and extracts constraints, target assets, and requested outcomes.
3. The system converts the request into a structured command plan.
4. The command plan is validated, routed to the appropriate tools, and executed.
5. Results are returned to the user with explanations, previews, or follow-up questions when needed.

## Agent Communication
- Agents communicate through a shared task model and event bus
- Each agent handles a specific layer of execution, such as planning, editing, validation, or export
- Agents can delegate work to other agents when the request requires multi-step reasoning

## Tool Use and Function Calling
- The AI system will rely on tool definitions for actions such as cutting clips, applying effects, generating captions, or exporting media
- Function calling will be used to map semantic intent to concrete operations
- The system will support retries, validation, and fallbacks for tool execution
- Provider abstraction will allow the same orchestration layer to work across Gemini, DeepSeek, and local models

## Safety and Control
- High-risk operations should require confirmation when necessary
- User edits should remain reversible and auditable
- AI-generated changes should be previewable before final application
