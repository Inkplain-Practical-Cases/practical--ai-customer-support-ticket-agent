# Step 2 of 6 — Classify support requests
## What you build in this step
Every ticket receives an intent and priority from a provider that can be fake (offline) or OpenAI (live).
## What you learn
- Provider interfaces and dependency injection
- Intent and priority classification
- Keeping HTTP routes free from AI SDK logic
## What changed since step 1
TicketView gains intent/priority and the handler calls service_classify_request before persistence. Providers added: FakeClassifier and OpenAIClassifier.
## Run it
```bash
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```
## Verify it
POST /tickets with an invoice message: expect intent=billing. "Urgent" messages get priority=urgent. To use OpenAI set CLASSIFIER_PROVIDER=openai and OPENAI_API_KEY.
## Diagram
STEP-2 is built in Simulator Stage 3.
## Next
Step 3 validates classifier output as a typed contract.
