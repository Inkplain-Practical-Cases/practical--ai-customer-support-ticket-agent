# Ticket orchestration: classify first, then ask the ticket service to store.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.services.service_create_ticket import service_create_ticket
from app.providers.tickets.base import TicketStore
from app.providers.classifier.base import Classifier
from app.features.feature_tickets.services.service_classify_request import service_classify_request

async def handle_create_ticket(payload: TicketCreate, store: TicketStore, classifier: Classifier) -> TicketView:
    classification = await service_classify_request(payload.message, classifier)
    return await service_create_ticket(payload, store, classification)
