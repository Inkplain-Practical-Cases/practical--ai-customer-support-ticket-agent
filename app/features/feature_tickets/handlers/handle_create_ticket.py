# Maps safe validation, timeout and storage errors to stable HTTP responses.
# Never sends raw LLM output or customer data into error messages or logs.
import asyncio
from fastapi import HTTPException
from pydantic import ValidationError
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.services.service_process_support_request import service_process_support_request
from app.features.feature_tickets.services.service_log_ticket_event import service_log_ticket_event
from app.providers.tickets.base import TicketStore
from app.providers.classifier.base import Classifier
from app.core.config import get_timeout_seconds
async def handle_create_ticket(payload: TicketCreate, store: TicketStore, classifier: Classifier) -> TicketView:
    try:
        record = await service_process_support_request(payload, store, classifier, get_timeout_seconds())
        service_log_ticket_event("created", record.id)
        return record
    except asyncio.TimeoutError as exc:
        service_log_ticket_event("model_timeout")
        raise HTTPException(status_code=504, detail="Support service timed out") from exc
    except (ValueError, ValidationError) as exc:
        service_log_ticket_event("invalid_model_output")
        raise HTTPException(status_code=502, detail="Invalid AI classification or tool call") from exc
    except Exception as exc:
        service_log_ticket_event("backend_unavailable")
        raise HTTPException(status_code=503, detail="Ticket storage temporarily unavailable") from exc
