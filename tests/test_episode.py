from foundry.runtime import Episode
from foundry.core.event import Event
from foundry.core.decision import Decision
def test_episode():
    e=Episode("test")
    e.record_event(Event(type="tick"))
    e.record_decision(Decision(actor_id="a",action="go"))
    e.finish()
    assert len(e.events)==1
    assert len(e.decisions)==1
