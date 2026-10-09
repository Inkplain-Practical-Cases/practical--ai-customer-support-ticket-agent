# In-memory store preserves classified tickets; lock serializes ticket IDs.
import asyncio
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
class InMemoryTicketStore:
    def __init__(self) -> None:
        self._records: list[TicketView] = []
        self._lock = asyncio.Lock()
    async def create(self, payload: TicketCreate, classification: dict) -> TicketView:
        async with self._lock:
            record = TicketView(id=len(self._records)+1, **payload.model_dump(), **classification)
            self._records.append(record)
            return record
