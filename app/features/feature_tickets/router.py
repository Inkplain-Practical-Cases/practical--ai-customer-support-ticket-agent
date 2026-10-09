# Door declares POST /tickets and injects shared providers; no AI calls here.
from fastapi import APIRouter, Depends
from app.core.dependencies import get_ticket_store, get_classifier
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
from app.features.feature_tickets.handlers.handle_create_ticket import handle_create_ticket
from app.providers.tickets.base import TicketStore
from app.providers.classifier.base import Classifier

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.post("", status_code=201, response_model=TicketView)
async def create_ticket(payload: TicketCreate, store: TicketStore = Depends(get_ticket_store), classifier: Classifier = Depends(get_classifier)) -> TicketView:
    return await handle_create_ticket(payload, store, classifier)
