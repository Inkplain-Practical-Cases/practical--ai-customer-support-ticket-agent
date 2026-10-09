# Orchestrates classification; returns HTTP 502 if the model produced unusable output.
from fastapi import HTTPException
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.services.service_create_ticket import service_create_ticket
from app.features.feature_tickets.services.service_classify_request import service_classify_request
from app.providers.tickets.base import TicketStore
from app.providers.classifier.base import Classifier
async def handle_create_ticket(payload: TicketCreate, store: TicketStore, classifier: Classifier) -> TicketView:
    try:
        classification = await service_classify_request(payload.message, classifier)
    except ValueError as exc:
        # Do not leak raw LLM content to end users; no ticket is written.
        raise HTTPException(status_code=502, detail="Invalid classification response") from exc
    return await service_create_ticket(payload, store, classification)
