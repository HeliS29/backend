from fastapi import Form
from pydantic import BaseModel, EmailStr
from typing import Optional,Dict,Any, Text
from datetime import datetime


class ReportResponse(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    manager_id: Optional[int]
    current_version_id: Optional[int]
    created_at:Optional[datetime] 
    updated_at: Optional[datetime] 
    detail:Optional[str]


class ReportCreate(BaseModel):
    user_id: int = Form(...)
    manager_id: int = Form(...)
    role: str = Form(...),
    file:str=Form(...)
    

class ReportVersionResponse(BaseModel):
    id: int
    report_id: int
    version_number: int
    generated_at: datetime
    pdf_path: str
    # manager_comments:Optional[Text]
  
class ManagerResponse(BaseModel):
    manager_id: int



class ReportContentResponse(BaseModel):
    user_id: int
    version_number: int
    content: Dict[str, Any]



class NotificationResponse(BaseModel):
    id: int
    user_id: Optional[int]
    manager_id: Optional[int]
    message: str
    is_read: bool
    created_at: datetime