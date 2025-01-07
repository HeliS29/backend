from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ReportVersionContentResponse(BaseModel):
    version_number: int
    content: dict

class EmailHistoryResponse(BaseModel):
    subject: str
    body: str
    status: str
    sent_at: str | None

class ReportHistoryResponse(BaseModel):
    report_history: List[ReportVersionContentResponse]
    email_history: List[EmailHistoryResponse]




# Define Pydantic models for response
class ReportVersionContentResponse(BaseModel):
    version_number: int
    content: dict

class EmailHistoryResponse(BaseModel):
    subject: str
    body: str
    status: str
    sent_at: str | None

class ReportHistoryResponse(BaseModel):
    report_history: List[ReportVersionContentResponse]
    email_history: List[EmailHistoryResponse]
