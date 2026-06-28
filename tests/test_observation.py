from foundry.core import Observation


def test_observation_attributes():

    observation = Observation(
        attributes={
            "temperature": 72,
            "humidity": 40,
        }
    )

    assert observation.attributes["temperature"] == 72
    assert observation.attributes["humidity"] == 40


def test_observation_defaults_metadata():

    observation = Observation(
        attributes={}
    )

    assert observation.metadata == {}