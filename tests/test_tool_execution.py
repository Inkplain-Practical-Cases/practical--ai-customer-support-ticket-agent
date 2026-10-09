# A model cannot rewrite customer identity or invent another tool operation.
import pytest
from pydantic import ValidationError
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate
from app.features.feature_tickets.schemas.tool_request import ToolRequest
from app.features.feature_tickets.services.service_validate_tool_args import service_validate_tool_args
from app.providers.classifier.fake_classifier import FakeClassifier
@pytest.mark.asyncio
async def test_fake_model_requests_trusted_tool() -> None:
    payload = TicketCreate(subject="Login issue",message="Cannot sign in now",email="alex@example.com")
    tool = ToolRequest.model_validate(await FakeClassifier().propose_tool(payload.model_dump(mode="json")))
    service_validate_tool_args(tool, payload)
def test_model_cannot_change_email() -> None:
    payload = TicketCreate(subject="Login issue",message="Cannot sign in now",email="alex@example.com")
    with pytest.raises(ValueError):
        service_validate_tool_args(ToolRequest(name="create_ticket",arguments={"subject":"Login issue","message":"Cannot sign in now","email":"attacker@example.com"}), payload)
def test_model_cannot_choose_unknown_tool() -> None:
    with pytest.raises(ValidationError):
        ToolRequest(name="delete_customer",arguments={})
