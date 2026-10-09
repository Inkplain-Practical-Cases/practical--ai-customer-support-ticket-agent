# In-memory learning adapter for one shared ticket store.
# Why it exists: the first step runs with no database.
# Without it: students need PostgreSQL before they can test the API skeleton.
import asyncio
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView

class InMemoryTicketStore:
    def __init__(self) -> None:
        self._records: list[TicketView] = []
        self._lock = asyncio.Lock()

    async def create(self, payload: TicketCreate) -> TicketView:
        # Lock guarantees unique sequential ticket IDs in concurrent requests.
        async with self._lock:
            record = TicketView(id=len(self._records) + 1, **payload.model_dump())
            self._records.append(record)
            return record
