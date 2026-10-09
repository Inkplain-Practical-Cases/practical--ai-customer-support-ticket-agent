# PostgreSQL adapter; parameterized SQL persists customers and tickets.
# Why it exists: real ticket history survives process restarts and concurrent workers.
# Without it: customer matching and ticket IDs are local to one Python process.
import asyncpg
from app.features.feature_tickets.schemas.ticket_schemas import TicketCreate, TicketView
class PostgresTicketStore:
    def __init__(self, database_url: str) -> None:
        # A single configured adapter is injected by the dependency factory.
        self.database_url = database_url

    async def ensure_customer(self, email: str) -> int:
        # ON CONFLICT handles two requests looking up the same email simultaneously.
        conn = await asyncpg.connect(self.database_url)
        try:
            return await conn.fetchval(
                """INSERT INTO customers(email) VALUES($1)
                   ON CONFLICT (email) DO UPDATE SET email=EXCLUDED.email
                   RETURNING id""", email
            )
        finally:
            await conn.close()

    async def create(self, payload: TicketCreate, classification: dict, customer_id: int | None = None) -> TicketView:
        conn = await asyncpg.connect(self.database_url)
        try:
            # Prepared placeholders prevent untrusted model text from becoming SQL code.
            new_id = await conn.fetchval(
                """INSERT INTO tickets(customer_id,subject,message,intent,priority,status)
                   VALUES($1,$2,$3,$4,$5,'open') RETURNING id""",
                customer_id, payload.subject, payload.message,
                classification["intent"], classification["priority"]
            )
            return TicketView(id=new_id, **payload.model_dump(), **classification)
        finally:
            await conn.close()
