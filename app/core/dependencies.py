# Builds a single configured model adapter and ticket-store adapter per process.
from functools import lru_cache
import os
from app.providers.tickets.in_memory_ticket_store import InMemoryTicketStore
from app.providers.tickets.postgres_ticket_store import PostgresTicketStore
from app.providers.classifier.fake_classifier import FakeClassifier
from app.providers.classifier.openai_classifier import OpenAIClassifier

@lru_cache
def get_ticket_store():
    # The database is opt-in: deterministic offline tests stay self-contained.
    if os.getenv("TICKET_STORE","memory") == "postgres":
        url = os.getenv("DATABASE_URL","")
        if not url:
            raise ValueError("DATABASE_URL must be configured for PostgreSQL")
        return PostgresTicketStore(url)
    return InMemoryTicketStore()

@lru_cache
def get_classifier():
    if os.getenv("CLASSIFIER_PROVIDER","fake") == "openai":
        key = os.getenv("OPENAI_API_KEY","")
        if not key:
            raise ValueError("OPENAI_API_KEY is required")
        return OpenAIClassifier(key,os.getenv("OPENAI_MODEL","gpt-4o-mini"))
    return FakeClassifier()
