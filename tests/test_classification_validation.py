# Invalid AI JSON, priority and extra keys must be rejected before ticket persistence.
import pytest
from app.features.feature_tickets.services.service_parse_classification import service_parse_classification
def test_valid_classification() -> None:
    value = service_parse_classification({"intent":"billing","priority":"normal"})
    assert value.intent == "billing"
@pytest.mark.parametrize("raw", ['not json', '{"intent":"sales","priority":"urgent"}', '{"intent":"billing","priority":"critical"}', '{"intent":"billing","priority":"normal","role":"admin"}'])
def test_reject_invalid_model_output(raw: str) -> None:
    with pytest.raises(ValueError):
        service_parse_classification(raw)
