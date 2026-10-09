# Makes model-suggested ticket data subordinate to the verified API request.
# Why it exists: the model must not change a customer's email or message.
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate
from app.features.feature_tickets.schemas.tool_request import ToolRequest
def service_validate_tool_args(tool: ToolRequest, payload: TicketCreate) -> None:
    # Never trust model-provided identity or text without comparing to input.
    expected = payload.model_dump(mode="json")
    if tool.name != "create_ticket" or tool.arguments != expected:
        raise ValueError("tool arguments do not match validated request")
