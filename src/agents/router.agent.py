from langchain.agents import initialize_agent, Tool, AgentType
from langchain_openai import OpenAI
from src.tools.primary_tool import primary_tool
# Import other tools similarly
from src.utils.config_loader import *  # Loads env

llm = OpenAI(temperature=0.7)

tools = [
    Tool(name="Primary", func=primary_tool, description="Use for core data queries."),
    # Add other Tool instances
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)