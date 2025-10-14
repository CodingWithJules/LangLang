from src.schemas.output_schema import ToolOutput

def primary_tool(query: str) -> ToolOutput:
    """Mock tool for primary data queries."""
    return ToolOutput(source="Primary", data=[{"content": f"Primary data on {query}.", "timestamp": "2025-10-10"}])
