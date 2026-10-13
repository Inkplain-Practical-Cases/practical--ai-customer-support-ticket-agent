# Step 6 of 6 — Harden and verify
## What you build in this step
A complete support agent with bounded model calls, safe HTTP errors, structured logs and integration tests.
## What you learn
- Timeout and backend error handling
- Structured logging without PII
- End-to-end tests and dependency overrides
## What changed since step 5
service_process_support_request, service_log_ticket_event and get_timeout_seconds added. The handler catches timeouts and application failures without leaking provider secrets.
## Run it
```bash
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```
## Verify it
POST a billing request and check intent=billing and a ticket ID. Offline tests verify invalid user input (422), malformed model tool arguments (502), and a timed-out classifier (504).
## Diagram
The STEP-6 tab is produced in Stage 3 after approval.
## Next
This is the final implementation; main will hold the same code and FINAL.crd.

## Database (Entity) Relations
PostgreSQL tables `customers` and `tickets` are retained in STEP-6. Refer to `STEP-6.erd` and the main .inkp tab `STEP-6-ERD`. `tickets.customer_id` is an optional BIGINT FK referencing `customers.id`; customer email is unique. This is the actual `database/init.sql` schema. STEP-1..3 use only memory storage and do not have PostgreSQL tables.
