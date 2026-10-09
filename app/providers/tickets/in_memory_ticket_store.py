# Deterministic in-memory provider remains the offline default for every step.
import asyncio
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
class InMemoryTicketStore:
    def __init__(self) -> None:
        self._records: list[TicketView] = []
        self._customers: dict[str,int] = {}
        self._lock = asyncio.Lock()

    async def ensure_customer(self, email: str) -> int:
        async with self._lock:
            key = email.lower()
            if key not in self._customers:
                self._customers[key] = len(self._customers) + 1
            return self._customers[key]

    async def create(self, payload: TicketCreate, classification: dict, customer_id: int | None = None) -> TicketView:
        async with self._lock:
            record = TicketView(id=len(self._records)+1, **payload.model_dump(), **classification)
            self._records.append(record)
            return record
