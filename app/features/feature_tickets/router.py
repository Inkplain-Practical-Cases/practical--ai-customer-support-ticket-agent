# Thin HTTP door: validates the request schema and delegates to one handler.
# Called by FastAPI; calls handle_create_ticket and the injected store.
from fastapi import APIRouter, Depends
from app.core.dependencies import get_ticket_store
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.handlers.handle_create_ticket import handle_create_ticket
from app.providers.tickets.base import TicketStore

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.post("", status_code=201, response_model=TicketView)
async def create_ticket(payload: TicketCreate, store: TicketStore = Depends(get_ticket_store)) -> TicketView:
    # The handler owns workflow decisions; the door only forwards validated data.
    return await handle_create_ticket(payload, store)
