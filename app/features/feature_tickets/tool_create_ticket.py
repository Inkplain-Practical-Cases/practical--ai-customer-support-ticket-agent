# Trusted public tool boundary; only verified server inputs reach persistence.
# Called by service_execute_ticket_tool after tool arguments have been checked.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.schemas.classification_result import ClassificationResult
from app.features.feature_tickets.services.service_create_ticket import service_create_ticket
from app.providers.tickets.base import TicketStore
async def tool_create_ticket(payload: TicketCreate, classification: ClassificationResult, store: TicketStore) -> TicketView:
    # Use the same ticket service and customer matching used in earlier steps.
    return await service_create_ticket(payload, store, classification)
