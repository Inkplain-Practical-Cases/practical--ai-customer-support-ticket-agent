# Request/response contracts for POST /tickets; Step 2 includes classifier fields.
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
    intent: str = "general"
    priority: str = "normal"
