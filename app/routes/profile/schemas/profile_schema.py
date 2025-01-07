from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class EmployeeCreate(BaseModel):
    
    manager_id: Optional[int] = None
    job_title: Optional[str] = None
    organization_id: Optional[int] = None

class EmployeeCreateresponse(BaseModel):
    user_id: int
    manager_id: int
    job_title: str
    organization_id: int

class EmployeeResponse(BaseModel):
  
    user_id: int
    manager_id: Optional[int] 
    name: str
    job_title: Optional[str] 
    organization_id: Optional[int] 
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class EmployeeResponseForUpdate(BaseModel):
    id: int
    manager_id: Optional[int] 
    job_title: Optional[str] 
    organization_id: Optional[int] 
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
class ManagerResponse(BaseModel):
    id: int
    email: str
    dept: Optional[str]
    name:str

    class Config:
        from_attributes = True


class OrganizationResponse(BaseModel):
    id: int
    name: str
    

    class Config:
        from_attributes = True


class ManagerCreate(BaseModel):
    name: str
    email: EmailStr
    dept: Optional[str] = None

    class Config:
        orm_mode = True



class OrganizationCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True