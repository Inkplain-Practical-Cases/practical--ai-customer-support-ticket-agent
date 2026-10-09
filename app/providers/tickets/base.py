# Provider interface: storage may be in-memory now and PostgreSQL in step 4.
from typing import Protocol
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView

class TicketStore(Protocol):
    async def create(self, payload: TicketCreate) -> TicketView: ...
