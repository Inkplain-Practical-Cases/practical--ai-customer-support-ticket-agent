# Emits structured application events without logging customer message bodies or keys.
import logging
logger = logging.getLogger("northstar.tickets")
def service_log_ticket_event(event: str, ticket_id: int | None = None) -> None:
    # Minimal event fields are enough to correlate success or failure safely.
    logger.info("ticket_event=%s ticket_id=%s", event, ticket_id if ticket_id is not None else "-")
