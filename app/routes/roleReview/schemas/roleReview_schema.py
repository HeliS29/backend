from typing import Any, Dict, Text
from pydantic import BaseModel,model_validator,Field,constr
from datetime import datetime


class RoleReviewCreate(BaseModel):
    user_id: int
    purpose: str
    name: str
    title: str
    organization: str
    date: datetime
    prepared_by: str
    # job_summary: str 
    job_summary: Text
    # class Config:
    #     from_attributes = True
    #     # Optional: Perform truncation if string length exceeds limit
    #     @staticmethod
    #     def validate_job_summary(value: str) -> str:
    #         return value[:1000] 


class RoleReviewUpdate(BaseModel):
    purpose: str = None
    name: str = None
    title: str = None
    organization: str = None
    date: datetime=None
    prepared_by: str = None
    job_summary: constr(max_length=1000) # type: ignore

    class Config:
        from_attributes = True



class RoleReviewResponse(BaseModel):
    id: int
    # user_id: int
    # purpose: str
    # name: str
    # title: str
    # organization: str
    # date: datetime
    # prepared_by: str
    job_summary: str
    created_at: datetime
    updated_at: datetime 

    class Config:
        from_attributes = True



