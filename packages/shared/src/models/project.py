from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class ProjectStatus(str, Enum):
    IDLE = "idle"
    EDITING = "editing"
    RENDERING = "rendering"
    EXPORTING = "exporting"
    ERROR = "error"


@dataclass(slots=True)
class TimelineState:
    timeline_id: str
    tracks: List[Dict[str, Any]] = field(default_factory=list)
    current_time: float = 0.0
    duration: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ProjectState:
    project_id: str
    name: str
    status: ProjectStatus = ProjectStatus.IDLE
    timeline: Optional[TimelineState] = None
    assets: List[str] = field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
