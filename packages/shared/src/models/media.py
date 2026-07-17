from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


class MediaType(str, Enum):
    VIDEO = "video"
    AUDIO = "audio"
    IMAGE = "image"
    TEXT = "text"
    TIMELINE = "timeline"


@dataclass(slots=True)
class MediaMetadata:
    duration: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None
    codec: Optional[str] = None
    frame_rate: Optional[float] = None
    sample_rate: Optional[int] = None
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class MediaAsset:
    id: str
    type: MediaType
    name: Optional[str] = None
    uri: Optional[str] = None
    metadata: MediaMetadata = field(default_factory=MediaMetadata)
    tags: list[str] = field(default_factory=list)
