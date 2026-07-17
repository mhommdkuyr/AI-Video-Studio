import sys
from pathlib import Path

# Add shared to path for internal service usage
shared_path = str(Path(__file__).resolve().parents[3] / "packages" / "shared" / "src")
if shared_path not in sys.path:
    sys.path.insert(0, shared_path)

from models.command import (
    ApprovalState,
    Command,
    CommandOperation,
    CommandStatus,
    CommandValidationResult,
    ValidationIssue,
)
from models.media import MediaAsset

# Alias for backward compatibility during transition if needed
ExecutionStatus = CommandStatus
CommandAsset = MediaAsset

__all__ = [
    "ApprovalState",
    "Command",
    "CommandOperation",
    "CommandStatus",
    "ExecutionStatus",
    "CommandValidationResult",
    "ValidationIssue",
    "CommandAsset",
]
