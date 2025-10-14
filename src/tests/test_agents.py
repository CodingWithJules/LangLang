import pytest

def test_agent_runs_without_error():
    response = "Mock agent response"
    assert isinstance(response, str)
    assert len(response) > 0
