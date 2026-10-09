# FastAPI assembly door; receives routers but owns no ticket business rules.
# Called by Uvicorn; delegates HTTP traffic to feature_tickets.router.
from fastapi import FastAPI
from app.features.feature_tickets.router import router

app = FastAPI(title="Northstar AI Customer Support Ticket Agent")
app.include_router(router)
