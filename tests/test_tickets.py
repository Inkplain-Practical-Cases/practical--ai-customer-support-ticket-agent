# Step-1 tests prove valid input creates a ticket and invalid input is rejected.
from fastapi.testclient import TestClient
from app.main import app

def test_create_ticket_success() -> None:
    with TestClient(app) as client:
        res = client.post("/tickets", json={"subject":"Login issue","message":"Cannot sign in to my account","email":"customer@example.com"})
        assert res.status_code == 201
        assert res.json()["status"] == "open"
        assert isinstance(res.json()["id"], int)

def test_invalid_ticket_returns_422() -> None:
    with TestClient(app) as client:
        res = client.post("/tickets", json={"subject":"x","message":"bad","email":"not-an-email"})
        assert res.status_code == 422
