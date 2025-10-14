import pytest
from src.tools.primary_tool import primary_tool
from src.tools.secondary_tool import secondary_tool
from src.schemas.output_schema import ToolOutput

def test_primary_tool_returns_valid_output():
    result = primary_tool("test query")
    assert isinstance(result, ToolOutput)
    assert result.source == "Primary"
    assert len(result.data) > 0
    assert "test query" in result.data[0]["content"]

def test_secondary_tool_returns_valid_output():
    result = secondary_tool("test query")
    assert isinstance(result, ToolOutput)
    assert result.source == "Secondary"
    assert len(result.data) > 0
    assert "test query" in result.data[0]["content"]
