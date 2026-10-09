# Step 4 of 6 — Persist tickets in PostgreSQL
## What you build in this step
Keep the offline memory provider while adding an opt-in PostgreSQL adapter and customer email matching. PostgreSQL preserves tickets across restarts.
## What you learn
- Database provider selection and injection
- Parameterized SQL and customer uniqueness
- Docker Compose for local PostgreSQL
## What changed since step 3
service_find_customer and PostgresTicketStore are added; the ticket service matches customer email before creating a ticket.
## Run it
```bash
pip install -r requirements.txt
pytest -q
docker compose up -d postgres
export TICKET_STORE=postgres
export DATABASE_URL=postgresql://northstar:local_dev_only@localhost:5432/northstar
uvicorn app.main:app --reload
```
## Verify it
Offline pytest includes customer matching. With Docker Postgres up, POST /tickets twice using the same email and verify one customer row and two ticket rows via psql.
## Diagram
STEP-4 is authored in Stage 3.
## Next
Step 5 adds trusted, backend-validated AI tool execution.
