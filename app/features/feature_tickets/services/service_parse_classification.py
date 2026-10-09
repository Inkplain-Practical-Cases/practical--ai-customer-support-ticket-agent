# Parses model output into the single approved classification contract.
# Called by service_classify_request after an LLM provider returns data.
import json
from pydantic import ValidationError
from app.features.feature_tickets.schemas.classification_result import ClassificationResult
def service_parse_classification(raw: dict | str) -> ClassificationResult:
    # Models can answer in text or dictionaries; both must pass the same schema.
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError("classifier output was not valid JSON") from exc
    try:
        return ClassificationResult.model_validate(raw)
    except ValidationError as exc:
        raise ValueError("classifier produced unsupported classification fields") from exc
