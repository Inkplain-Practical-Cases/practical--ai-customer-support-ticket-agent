# Stable classifier interface: feature services depend on it, not on an SDK.
from typing import Protocol
class Classifier(Protocol):
    async def classify(self, message: str) -> dict: ...
