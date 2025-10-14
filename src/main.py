from src.agents.router_agent import agent
from src.utils.aggregator import aggregate_results

def run_agentic_query(user_query: str) -> str:
    response = agent.run(f"Query: {user_query}. Use relevant tools and aggregate.")
    return response  # Or apply aggregate_results

if __name__ == "__main__":
    query = "Sample query for data integration"
    result = run_agentic_query(query)
    print(result)