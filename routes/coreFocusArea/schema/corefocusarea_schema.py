from pydantic import BaseModel,model_validator
from datetime import datetime
from typing import Optional


class CoreFocusAreaUpdate(BaseModel):
    id:int
    area: str = None
    time_spent: float = None
    importance: float = None
    

    class Config:
        orm_mode = True


class CoreFocusAreaCreate(BaseModel):
    area: str
    time_spent: float
    importance: float
    user_id: int

    class Config:
        orm_mode = True

class CoreFocusAreaResponse(BaseModel):
    id:int
    area: str
    time_spent: float
    importance: float
    user_id: int
    # message:Optional[str]

    class Config:
        orm_mode = True