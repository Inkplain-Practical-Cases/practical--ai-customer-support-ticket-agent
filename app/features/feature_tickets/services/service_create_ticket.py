# Persists only a typed, validated classification.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.schemas.classification_result import ClassificationResult
from app.providers.tickets.base import TicketStore
async def service_create_ticket(payload: TicketCreate, store: TicketStore, classification: ClassificationResult) -> TicketView:
    # A validated typed object replaces step 2's untrusted dict.
    return await store.create(payload, classification.model_dump())
