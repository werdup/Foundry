from dataclasses import dataclass,field
from uuid import uuid4,UUID
from typing import Any
from .jsonable import to_jsonable
@dataclass(frozen=True)
class Decision:
    actor_id:str
    action:str
    reason:str=""
    parameters:dict[str,Any]=field(default_factory=dict)
    confidence:float=1.0
    id:UUID=field(default_factory=uuid4)
    def to_dict(self): return to_jsonable(self)
