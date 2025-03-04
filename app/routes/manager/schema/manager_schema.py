from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    job_title: Optional[str]
    role:str
    # organization_id: Optional[int]

    class Config:
        from_attributes = True