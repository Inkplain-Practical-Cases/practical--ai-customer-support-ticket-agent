# Creates a ticket record through an injected storage interface.
# Why it exists: business ticket creation stays separate from HTTP and storage.
# Without it: persistence and API orchestration would become entangled.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.providers.tickets.base import TicketStore

async def service_create_ticket(payload: TicketCreate, store: TicketStore) -> TicketView:
    # Store generates the ticket ID, so every provider follows the same contract.
    return await store.create(payload)
