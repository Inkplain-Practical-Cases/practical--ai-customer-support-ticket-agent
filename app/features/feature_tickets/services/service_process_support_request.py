# One complete support request pipeline: classification followed by verified tool execution.
# Why it exists: HTTP errors stay in the handler while business steps stay testable.
import asyncio
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.services.service_classify_request import service_classify_request
from app.features.feature_tickets.services.service_execute_ticket_tool import service_execute_ticket_tool
from app.providers.tickets.base import TicketStore
from app.providers.classifier.base import Classifier
async def service_process_support_request(payload: TicketCreate, store: TicketStore, classifier: Classifier, timeout_seconds: float) -> TicketView:
    # Bound model classification and tool proposal so a stalled SDK cannot hold requests forever.
    classification = await asyncio.wait_for(service_classify_request(payload.message, classifier), timeout=timeout_seconds)
    return await asyncio.wait_for(service_execute_ticket_tool(payload, classification, store, classifier), timeout=timeout_seconds)
