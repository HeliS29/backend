from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommentCreate(BaseModel):
    
    user_id: int
    report_version_id: int
    comment_text: Optional[str]=None


class CommentResponse(BaseModel):
    id: int
    user_id: int
    report_version_id: int
    comment_text: str
    created_at: datetime

class CommentUpdate(BaseModel):
    comment_text: str