# AI Customer Support Ticket Agent

A beginner Inkplain practical case for fictional SaaS company Northstar Support. Incoming customer tickets are classified by a fake or OpenAI model, validated with Pydantic, matched to customers and stored in memory or PostgreSQL. Backend-validated tool calls protect customer-submitted data.

## The six cumulative steps

| Step | Branch | Capability |
|---|---|---|
| 1 | step-01-receive-and-store-tickets | FastAPI ticket API and memory store |
| 2 | step-02-classify-support-requests | Fake/OpenAI intent and priority |
| 3 | step-03-validate-ai-output | Strict typed model result |
| 4 | step-04-persist-tickets-in-postgresql | Customer matching and PostgreSQL persistence |
| 5 | step-05-invoke-ticket-tools | Trusted create_ticket tool |
| 6 | step-06-harden-and-verify | Timeouts, safe errors, logs and integration tests |

Each branch runs from its own source and has `STEP-N.crd` and `STEP-N.md`, describing its full current state. Main is the final version and has `FINAL.crd`. The Stage-3 Simulator export `ai-customer-support-ticket-agent.inkp` will be created later, not during this stage.

## Local offline run (Python 3.12+)
```bash
git clone https://github.com/Inkplain-Practical-Cases/practical--ai-customer-support-ticket-agent.git
cd practical--ai-customer-support-ticket-agent
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```

Then submit:
```bash
curl -X POST http://localhost:8000/tickets \
  -H "Content-Type: application/json" \
  -d '{"subject":"Billing issue","message":"Urgent refund of my invoice","email":"alex@example.com"}'
```

Expect HTTP 201 with `id`, `status=open`, `intent=billing` and `priority=urgent`. HTTP 422 rejects invalid input; 502 rejects invalid model output or tool arguments; 504 represents an AI timeout; 503 represents unavailable storage.

## Optional PostgreSQL
```bash
docker compose up -d postgres
export TICKET_STORE=postgres
export DATABASE_URL=postgresql://northstar:local_dev_only@localhost:5432/northstar
uvicorn app.main:app --reload
```
PostgreSQL is optional for offline pytest; `database/init.sql` bootstraps tables on fresh volumes. The local Docker password is for examples only and must be replaced outside development.

## Optional OpenAI
Set `CLASSIFIER_PROVIDER=openai` and `OPENAI_API_KEY` in your environment. The offline fake provider needs no key. The actual client also issues an SDK tool call; the backend always verifies the exact tool action and arguments.

## Structure and diagrams
Inkplain Codebase Structure: `router.py` door → `handle_create_ticket.py` handler → single-purpose `service_*` functions → injected classifier and storage providers. `STEP-N.crd` on each branch contains the Component Relation Diagram. The Simulator `.inkp` file is intentionally reserved for Stage 3.
