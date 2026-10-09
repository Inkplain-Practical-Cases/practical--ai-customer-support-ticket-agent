# Step 1 of 6 — Receive and store tickets

## What you build in this step
Build a FastAPI ticket endpoint with typed Pydantic requests and an in-memory provider. No external AI service or database is required.

## What you learn
- Keeping the API router a thin door
- Using a handler and single-purpose ticket service
- Validating requests and injecting a provider

## What changed since step 0
All eight CRD components are new; the API receives a request, validates it and stores an open ticket.

## Run it
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -q
```

## Verify it
```bash
curl -X POST http://localhost:8000/tickets -H 'Content-Type: application/json' -d '{"subject":"Login issue","message":"Cannot sign in to my account","email":"customer@example.com"}'
```
Expect HTTP 201 with integer id and status open; malformed bodies return HTTP 422.

## Diagram
Simulator STEP-1 will be created in Stage 3 from STEP-1.crd.

## Next
Step 2 adds support message classification.
