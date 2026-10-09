# Final offline endpoint tests cover intent, priority, validation and tool actions.
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.dependencies import get_classifier, get_ticket_store
from app.providers.classifier.fake_classifier import FakeClassifier
from app.providers.tickets.in_memory_ticket_store import InMemoryTicketStore
def test_end_to_end_ticket_creation():
    app.dependency_overrides[get_classifier] = lambda: FakeClassifier()
    app.dependency_overrides[get_ticket_store] = lambda: InMemoryTicketStore()
    try:
        with TestClient(app) as client:
            response = client.post("/tickets",json={"subject":"Billing issue","message":"Urgent refund for my invoice","email":"alex@example.com"})
        assert response.status_code == 201, response.text
        assert response.json()["intent"] == "billing"
        assert response.json()["priority"] == "urgent"
    finally:
        app.dependency_overrides.clear()
def test_reject_bad_input_before_llm():
    with TestClient(app) as client:
        result = client.post("/tickets", json={"subject":"","message":"short","email":"bad"})
    assert result.status_code == 422
def test_timeout_returns_504():
    class SlowClassifier(FakeClassifier):
        async def classify(self,message):
            import asyncio
            await asyncio.sleep(0.1)
            return await super().classify(message)
    import os
    previous = os.environ.get("MODEL_TIMEOUT_SECONDS")
    os.environ["MODEL_TIMEOUT_SECONDS"] = "0.001"
    app.dependency_overrides[get_classifier] = lambda: SlowClassifier()
    app.dependency_overrides[get_ticket_store] = lambda: InMemoryTicketStore()
    try:
        with TestClient(app) as client:
            result = client.post("/tickets",json={"subject":"Login issue","message":"I cannot login today","email":"alex@example.com"})
        assert result.status_code == 504
    finally:
        app.dependency_overrides.clear()
        if previous is None:
            os.environ.pop("MODEL_TIMEOUT_SECONDS",None)
        else:
            os.environ["MODEL_TIMEOUT_SECONDS"] = previous
