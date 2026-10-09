# Malicious tool selection must stop before a ticket is stored.
from fastapi.testclient import TestClient
from app.main import app
from app.core.dependencies import get_classifier, get_ticket_store
from app.providers.classifier.fake_classifier import FakeClassifier
from app.providers.tickets.in_memory_ticket_store import InMemoryTicketStore
def test_tool_mutated_email_is_rejected():
    class MaliciousClassifier(FakeClassifier):
        async def propose_tool(self, validated_ticket):
            altered = dict(validated_ticket)
            altered["email"] = "attacker@example.org"
            return {"name":"create_ticket","arguments":altered}
    store = InMemoryTicketStore()
    app.dependency_overrides[get_classifier] = lambda: MaliciousClassifier()
    app.dependency_overrides[get_ticket_store] = lambda: store
    try:
        with TestClient(app) as client:
            response = client.post("/tickets",json={"subject":"Login issue","message":"Cannot sign in today","email":"alex@example.com"})
        assert response.status_code == 502
        assert len(store._records) == 0
    finally:
        app.dependency_overrides.clear()
