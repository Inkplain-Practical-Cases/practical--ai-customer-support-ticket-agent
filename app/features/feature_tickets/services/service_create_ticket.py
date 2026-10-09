# Persists a validated classification and resolves a customer before creating the ticket.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.schemas.classification_result import ClassificationResult
from app.features.feature_tickets.services.service_find_customer import service_find_customer
from app.providers.tickets.base import TicketStore
async def service_create_ticket(payload: TicketCreate, store: TicketStore, classification: ClassificationResult) -> TicketView:
    # Customer matching and ticket creation share one injected repository contract.
    customer_id = await service_find_customer(str(payload.email), store)
    return await store.create(payload, classification.model_dump(), customer_id)
