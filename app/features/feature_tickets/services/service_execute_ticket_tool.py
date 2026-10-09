# Orchestrates AI tool selection and a trusted ticket creation operation.
# The model chooses a named action; the application enforces the arguments.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.schemas.classification_result import ClassificationResult
from app.features.feature_tickets.schemas.tool_request import ToolRequest
from app.features.feature_tickets.services.service_validate_tool_args import service_validate_tool_args
from app.features.feature_tickets.tool_create_ticket import tool_create_ticket
from app.providers.tickets.base import TicketStore
from app.providers.classifier.base import Classifier
async def service_execute_ticket_tool(payload: TicketCreate, classification: ClassificationResult, store: TicketStore, classifier: Classifier) -> TicketView:
    # Tool suggestions are untrusted until checked against original request.
    suggestion = await classifier.propose_tool(payload.model_dump(mode="json"))
    request = ToolRequest.model_validate(suggestion)
    service_validate_tool_args(request, payload)
    return await tool_create_ticket(payload, classification, store)
