from pydantic import BaseModel, Field

class ToolOutput(BaseModel):
    source: str = Field(description="Tool source name")
    data: list = Field(description="List of data items, e.g., [{'content': 'item', 'timestamp': 'date'}]")
