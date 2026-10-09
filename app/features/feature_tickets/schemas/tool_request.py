# Tool request contract permits exactly the supported ticket action.
from typing import Literal
from pydantic import BaseModel, ConfigDict
class ToolRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: Literal["create_ticket"]
    arguments: dict
