# Persists a classified ticket through the TicketStore interface.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.providers.tickets.base import TicketStore

async def service_create_ticket(payload: TicketCreate, store: TicketStore, classification: dict) -> TicketView:
    return await store.create(payload, classification)
