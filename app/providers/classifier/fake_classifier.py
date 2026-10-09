# Deterministic model double: classifies Northstar ticket text without network calls.
# Why it exists: students can reproduce results offline and debug intent routing.
class FakeClassifier:
    async def classify(self, message: str) -> dict:
        text = message.lower()
        if any(word in text for word in ("invoice", "payment", "billing", "refund")):
            intent = "billing"
        elif any(word in text for word in ("login", "password", "sign in", "account")):
            intent = "account_access"
        elif any(word in text for word in ("error", "crash", "bug", "broken")):
            intent = "technical"
        else:
            intent = "general"
        priority = "urgent" if any(word in text for word in ("urgent", "outage", "blocked")) else "normal"
        return {"intent": intent, "priority": priority}
