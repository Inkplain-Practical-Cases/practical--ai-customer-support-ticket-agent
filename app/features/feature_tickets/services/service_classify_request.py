# Single job: delegate classification of a ticket message to the injected provider.
from app.providers.classifier.base import Classifier

async def service_classify_request(message: str, classifier: Classifier) -> dict:
    return await classifier.classify(message)
