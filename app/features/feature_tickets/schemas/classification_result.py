# Strict structured LLM result; rejects invented categories and unsupported priority values.
# Why it exists: bad model output must not silently turn into a ticket.
from typing import Literal
from pydantic import BaseModel, ConfigDict
class ClassificationResult(BaseModel):
    model_config = ConfigDict(extra="forbid")
    intent: Literal["billing","account_access","technical","general"]
    priority: Literal["normal","urgent"]
