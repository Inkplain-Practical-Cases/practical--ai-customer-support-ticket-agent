# Coordinates a validated support request and delegates ticket construction.
# Called by POST /tickets; calls service_create_ticket without accessing storage internals.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.services.service_create_ticket import service_create_ticket
from app.providers.tickets.base import TicketStore

async def handle_create_ticket(payload: TicketCreate, store: TicketStore) -> TicketView:
    # One request becomes one service call; later steps add classification here.
    return await service_create_ticket(payload, store)
