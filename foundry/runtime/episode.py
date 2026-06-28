from dataclasses import dataclass,field
from datetime import datetime,timezone
from enum import StrEnum
from uuid import uuid4,UUID
from typing import Any
from foundry.core.event import Event
from foundry.core.decision import Decision
from foundry.core.jsonable import to_jsonable
class EpisodeState(StrEnum):
    CREATED="created"; STARTED="started"; FINISHED="finished"
@dataclass
class Episode:
    environment_name:str
    seed:int|None=None
    metadata:dict[str,Any]=field(default_factory=dict)
    id:UUID=field(default_factory=uuid4)
    state:EpisodeState=EpisodeState.CREATED
    started_at:datetime|None=None
    finished_at:datetime|None=None
    events:list[Event]=field(default_factory=list)
    decisions:list[Decision]=field(default_factory=list)
    def start(self):
        if self.started_at is None: self.started_at=datetime.now(timezone.utc)
        self.state=EpisodeState.STARTED
    def _check(self):
        if self.state==EpisodeState.FINISHED: raise RuntimeError("Episode finished")
        if self.state==EpisodeState.CREATED: self.start()
    def record_event(self,e:Event): self._check(); self.events.append(e)
    def record_decision(self,d:Decision): self._check(); self.decisions.append(d)
    def finish(self):
        if self.state==EpisodeState.CREATED: self.start()
        self.finished_at=datetime.now(timezone.utc); self.state=EpisodeState.FINISHED
    def summary(self):
        return {"id":str(self.id),"environment_name":self.environment_name,"seed":self.seed,
        "events":len(self.events),"decisions":len(self.decisions),"metadata":to_jsonable(self.metadata)}
