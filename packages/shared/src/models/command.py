from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class CommandStatus(str, Enum):
    PENDING = "pending"
    PLANNED = "planned"
    APPROVED = "approved"
    EXECUTING = "executing"
    VALIDATING = "validating"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"


class CommandType(str, Enum):
    EDIT = "edit"
    ANALYZE = "analyze"
    GENERATE = "generate"
    REVIEW = "review"
    EXPORT = "export"


class ApprovalState(str, Enum):
    AUTO = "auto"
    REVIEW = "review"
    EXPLICIT = "explicit"


@dataclass(slots=True)
class CommandParameter:
    name: str
    value: Any
    type: str = "string"


@dataclass(slots=True)
class CommandOperation:
    id: str
    type: str
    parameters: Dict[str, Any] = field(default_factory=dict)
    depends_on: Optional[List[str]] = None


@dataclass(slots=True)
class Command:
    command_id: str
    session_id: str
    actor_id: str
    intent: str
    assets: List[Any] = field(default_factory=list)  # Using Any to avoid circular import with media.py
    operations: List[CommandOperation] = field(default_factory=list)
    parameters: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0
    approval_state: ApprovalState = ApprovalState.AUTO
    status: CommandStatus = CommandStatus.PENDING
    schema_version: str = "1.0"
    source: str = "user"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class CommandResult:
    command_id: str
    status: CommandStatus
    output: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None


@dataclass(slots=True)
class ValidationIssue:
    code: str
    message: str


@dataclass(slots=True)
class CommandValidationResult:
    valid: bool
    issues: List[ValidationIssue] = field(default_factory=list)
