from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# class EmployeeCreate(BaseModel):
    
#     manager_id: Optional[int] = None
#     job_title: Optional[str] = None
#     organization_id: Optional[int] = None
class EmployeeCreate(BaseModel):
    job_title: Optional[str] = None
    company_name: Optional[str] = None
    purpose: Optional[str] = None
    manager_id: Optional[int] = None

    class Config:
        orm_mode = True

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


# class EmployeeResponseForUpdate(BaseModel):
#     id: int
#     manager_id: Optional[int] 
#     job_title: Optional[str] 
#     organization_id: Optional[int] 
#     created_at: datetime
#     updated_at: datetime
class EmployeeResponseForUpdate(BaseModel):
    id: int
    job_title: str
    # company_name: str
    # manager_id:int 
    purpose: str
    updated_at: datetime
    

    class Config:
        from_attributes = True
# class ManagerResponse(BaseModel):
#     id: int
#     email: str
#     dept: Optional[str]
#     name:str

#     class Config:
#         from_attributes = True
class ManagerCreate(BaseModel):
    name: str
    email: str
    password: str
    job_title:str  # Ensure password is hashed in the backend before saving
    # organization_id: int  # FK to the Organization table
     # Optional field for phone number

    class Config:
        orm_mode = True

# Schema for manager response
class ManagerResponse(BaseModel):
    id: int
    name: str
    email: str
    organization_id: int
    
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class OrganizationResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True


# class ManagerCreate(BaseModel):
#     name: str
#     email: EmailStr
#     dept: Optional[str] = None

#     class Config:
#         from_attributes = True

class OrganizationNameResponse(BaseModel):
    organization_name: str
    
class OrganizationCreate(BaseModel):
    organization_name: str
    manager_email:EmailStr
    manager_password:str
    manager_name:str
    class Config:
        from_attributes = True


class NewEmployeeCreate(BaseModel):
    name: str
    email: str
    job_title:str
    # password: str  # In production, make sure to handle password securely
class ResendEmail(BaseModel):
    name: str
    email: str 
   
class updateDetails(BaseModel):
    token: str 
    job_title: Optional[str]
    purpose: Optional[str] 

class NewEmployeeResponse(BaseModel):
    email: str
    name: str
class resendEmailResponse(BaseModel):
    message: str
    user_id: int
    email: str
    name: str


class RegistrationReq(BaseModel):
    token: str 
    password: str 
    job_title: Optional[str] = None
    purpose: Optional[str] =None
    organization_id:int

class LinkRegistrationResponse(BaseModel):
    message: str
    status: str = "success" 

class CurrentUserInfoResponse(BaseModel):
    name: str # User's name
    email: EmailStr # User's email
    job_title: Optional[str]  # User's job title
    company_name: str 
    manager_name:str 
    manager_email:EmailStr# Organization name as company_name
    purpose: Optional[str]
