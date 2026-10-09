# Resolves a customer record by email through the ticket-store boundary.
# This keeps SQL and database clients out of the workflow handler.
from app.providers.tickets.base import TicketStore
async def service_find_customer(email: str, store: TicketStore) -> int:
    return await store.ensure_customer(email)
