from src.schemas.output_schema import ToolOutput

def aggregate_results(results: list[ToolOutput]) -> str:
    aggregated = ""
    for result in results:
        aggregated += f"\nFrom {result.source}:\n"
        for item in result.data:
            aggregated += f"- {item['content']} (Timestamp: {item['timestamp']})\n"
    return aggregated