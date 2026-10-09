# Step 3 of 6 — Validate AI output
## What you build in this step
Classified messages now pass through a strict Pydantic schema. Malformed JSON or unsupported intent/priority cannot be persisted.
## What you learn
- JSON parsing and typed structured output
- Pydantic Literal fields and rejecting extra keys
- Failing closed on invalid model output
## What changed since step 2
ClassificationResult and service_parse_classification are added. service_classify_request converts untrusted model output to a verified schema.
## Run it
```bash
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```
## Verify it
The test_classification_validation suite rejects malformed JSON, unrecognized intent, unsupported priority and unexpected keys. A bad classifier response returns HTTP 502 and does not persist a ticket.
## Diagram
STEP-3 will be drawn in Stage 3.
## Next
Step 4 uses PostgreSQL for persistent tickets and customer matching.
