from pydantic import BaseModel,model_validator,Field
from datetime import datetime


class RoleReviewCreate(BaseModel):
    user_id: int
    purpose: str
    name: str
    title: str
    organization: str
    date: datetime
    prepared_by: str
    job_summary: str

    class Config:
        orm_mode = True


class RoleReviewUpdate(BaseModel):
    purpose: str = None
    name: str = None
    title: str = None
    organization: str = None
    date: datetime=None
    prepared_by: str = None
    job_summary: str = None

    class Config:
        orm_mode = True



class RoleReviewResponse(BaseModel):
    id: int
    user_id: int
    purpose: str
    name: str
    title: str
    organization: str
    date: datetime
    prepared_by: str
    job_summary: str
    created_at: datetime
    updated_at: datetime 

    class Config:
        orm_mode = True



