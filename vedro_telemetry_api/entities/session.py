from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, TypedDict
from uuid import UUID

__all__ = ("SessionEntity",)


class InterruptedException(TypedDict):
    type: str
    message: str
    traceback: str


class Environment(TypedDict):
    python_version: str
    vedro_version: str


_utc_zero = datetime.utcfromtimestamp(0)


@dataclass
class SessionEntity:
    id: UUID
    inited_at: datetime = _utc_zero
    created_at: datetime = _utc_zero

    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    project_id: str = ""

    discovered: Optional[int] = None
    scheduled: Optional[int] = None
    total: Optional[int] = None
    passed: Optional[int] = None
    failed: Optional[int] = None
    skipped: Optional[int] = None

    cmd: Optional[List[str]] = None
    environment: Optional[Environment] = None
    interrupted: Optional[InterruptedException] = None
