# Provides one shared ticket store to request handlers.
# Why it exists: routes do not create mutable storage for each request.
# Without it: a newly created ticket would disappear between requests.
from functools import lru_cache
from app.providers.tickets.in_memory_ticket_store import InMemoryTicketStore

@lru_cache
def get_ticket_store() -> InMemoryTicketStore:
    # Cache once so state persists across requests while learning.
    return InMemoryTicketStore()
