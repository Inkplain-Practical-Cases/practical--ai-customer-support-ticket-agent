# Stable storage interface supports the model classification fields.
from typing import Protocol
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
class TicketStore(Protocol):
    async def create(self, payload: TicketCreate, classification: dict) -> TicketView: ...
