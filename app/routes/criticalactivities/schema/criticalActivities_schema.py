from pydantic import BaseModel, Field, conint, constr
from typing import Optional


class CriticalActivityCreate(BaseModel):
    user_id: int 
    core_focus_area_id: int 
    area: str 
    importance: float 

class CriticalActivityUpdate(BaseModel):
    area: Optional[str] 
    importance: Optional[float] 
    core_focus_area_id: Optional[int] 

class CriticalActivityResponse(BaseModel):
    id: int
    user_id: int
    core_focus_area_id: int
    area: str
    importance: float

    class Config:
        from_attributes = True
