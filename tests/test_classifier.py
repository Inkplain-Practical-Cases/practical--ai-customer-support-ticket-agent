# Step 2: fake model classification is deterministic and testable without a key.
import pytest
from app.providers.classifier.fake_classifier import FakeClassifier
@pytest.mark.asyncio
async def test_billing_intent() -> None:
    result = await FakeClassifier().classify("Urgent: refund my invoice please")
    assert result == {"intent":"billing", "priority":"urgent"}
@pytest.mark.asyncio
async def test_account_access_intent() -> None:
    result = await FakeClassifier().classify("I cannot login to my account")
    assert result["intent"] == "account_access"
