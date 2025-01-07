from datetime import datetime
from pydantic import BaseModel

class EmailRequest(BaseModel):
    recipient_id: int
    recipient_type: str
    subject: str
    body: str
    sent_at:datetime