# Pydantic input/output contracts; reject missing or blank customer requests.
# Why it exists: callers must not store malformed messages.
from pydantic import BaseModel, Field, EmailStr

class TicketCreate(BaseModel):
    subject: str = Field(min_length=3, max_length=160)
    message: str = Field(min_length=5, max_length=4000)
    email: EmailStr

class TicketView(BaseModel):
    id: int
    subject: str
    message: str
    email: EmailStr
    status: str = "open"
