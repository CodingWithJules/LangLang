from langchain.agents import initialize_agent, Tool, AgentType
from langchain_openai import OpenAI
from src.tools.primary_tool import primary_tool
from src.tools.secondary_tool import secondary_tool
from src.utils.config_loader import *

llm = OpenAI(temperature=0.7)

tools = [
    Tool(name="Primary", func=primary_tool, description="Use for core data queries."),
    Tool(name="Secondary", func=secondary_tool, description="Use for secondary data queries.")
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
