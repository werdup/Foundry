from dataclasses import dataclass,field
from datetime import datetime,timezone
from uuid import uuid4,UUID
from typing import Any
from .jsonable import to_jsonable
@dataclass(frozen=True)
class Event:
    type:str
    payload:dict[str,Any]=field(default_factory=dict)
    timestamp:datetime=field(default_factory=lambda:datetime.now(timezone.utc))
    id:UUID=field(default_factory=uuid4)
    def to_dict(self): return to_jsonable(self)
