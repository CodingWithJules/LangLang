from src.schemas.output_schema import ToolOutput

def secondary_tool(query: str) -> ToolOutput:
    """Mock tool for secondary data queries."""
    return ToolOutput(source="Secondary", data=[{"content": f"Secondary data on {query}.", "timestamp": "2025-10-11"}])
