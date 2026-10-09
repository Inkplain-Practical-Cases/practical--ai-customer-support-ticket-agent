# Coordinates classification and trusted ticket tool execution.
from fastapi import HTTPException
from pydantic import ValidationError
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.services.service_classify_request import service_classify_request
from app.features.feature_tickets.services.service_execute_ticket_tool import service_execute_ticket_tool
from app.providers.tickets.base import TicketStore
from app.providers.classifier.base import Classifier
async def handle_create_ticket(payload: TicketCreate, store: TicketStore, classifier: Classifier) -> TicketView:
    try:
        classification = await service_classify_request(payload.message, classifier)
        return await service_execute_ticket_tool(payload, classification, store, classifier)
    except (ValueError, ValidationError) as exc:
        # A rejected tool call must not persist a ticket.
        raise HTTPException(status_code=502, detail="Invalid AI classification or tool call") from exc
