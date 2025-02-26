from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from typing import Union

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role:str
    

class UserLogin(BaseModel):
    
    # email: 
    name:str
    password: str
    role: Optional[str]
    organization_id:Optional[int]=None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

class UserResponsenew(BaseModel):
   
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

# class TokenResponse(BaseModel):
#     user_id: Optional[int] = None
#     manager_id: Optional[int] = None
#     role: str
#     token: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user_id:Optional[int] = None
    manager_id: Optional[int] = None
    role:str
    organization_id:Optional[int]=None
# class TokenResponse(BaseModel):
#     user_id: int
#     role: str
#     token: str
#     manager_id: Optional[int] = None
    

#     class Config:
#         from_attributes = True


class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirm(BaseModel):
    email: EmailStr
    verification_code: str
    new_password: str