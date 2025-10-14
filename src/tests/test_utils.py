import pytest
from src.utils.aggregator import aggregate_results
from src.schemas.output_schema import ToolOutput

@pytest.fixture
def sample_results():
    return [ToolOutput(source="Test", data=[{"content": "data", "timestamp": "now"}])]

def test_aggregator(sample_results):
    result = aggregate_results(sample_results)
    assert "From Test:" in result