# Validates the result of an injected model before ticket creation begins.
from app.providers.classifier.base import Classifier
from app.features.feature_tickets.schemas.classification_result import ClassificationResult
from app.features.feature_tickets.services.service_parse_classification import service_parse_classification
async def service_classify_request(message: str, classifier: Classifier) -> ClassificationResult:
    # Refuse invalid provider outputs before any persistence service is invoked.
    raw = await classifier.classify(message)
    return service_parse_classification(raw)
