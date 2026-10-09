# Builds and caches providers once so HTTP handlers never instantiate SDK clients.
from functools import lru_cache
import os
from app.providers.tickets.in_memory_ticket_store import InMemoryTicketStore
from app.providers.classifier.fake_classifier import FakeClassifier
from app.providers.classifier.openai_classifier import OpenAIClassifier

@lru_cache
def get_ticket_store() -> InMemoryTicketStore:
    return InMemoryTicketStore()

@lru_cache
def get_classifier():
    if os.getenv("CLASSIFIER_PROVIDER", "fake") == "openai":
        key = os.getenv("OPENAI_API_KEY", "")
        if not key:
            raise ValueError("OPENAI_API_KEY is required for the openai provider")
        return OpenAIClassifier(key, os.getenv("OPENAI_MODEL", "gpt-4o-mini"))
    return FakeClassifier()
