from dataclasses import asdict,is_dataclass
from datetime import datetime
from uuid import UUID
def to_jsonable(v):
    if is_dataclass(v): return {k:to_jsonable(x) for k,x in asdict(v).items()}
    if isinstance(v,dict): return {k:to_jsonable(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [to_jsonable(x) for x in v]
    if isinstance(v,(datetime,UUID)): return str(v)
    return v
