# In-memory contract proves repeated email messages map to the same customer.
import pytest
from app.providers.tickets.in_memory_ticket_store import InMemoryTicketStore
@pytest.mark.asyncio
async def test_matches_customer_case_insensitively():
    store = InMemoryTicketStore()
    a = await store.ensure_customer("Alex@Example.com")
    b = await store.ensure_customer("alex@example.com")
    assert a == b
@pytest.mark.asyncio
async def test_ticket_references_classification():
    from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate
    store = InMemoryTicketStore()
    user = await store.ensure_customer("alex@example.com")
    record = await store.create(TicketCreate(subject="Login issue",message="Cannot sign in",email="alex@example.com"),{"intent":"account_access","priority":"urgent"},user)
    assert record.priority == "urgent"
