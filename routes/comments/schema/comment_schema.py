from pydantic import BaseModel,root_validator,Field
from datetime import datetime
from typing import Optional

class CommentCreate(BaseModel):
    
    user_id: int
    report_version_id: int
    # comment_text: str
    comment_text: str

    # Using field_validator for comment_text field validation
    @root_validator(pre=True)
    def check_comment_text_not_empty(cls, values):
        comment_text = values.get("comment_text")
        if not comment_text or comment_text.strip() == "":
            raise ValueError("Comment content cannot be empty")
        return values
    


class CommentResponse(BaseModel):
    id: int
    user_id: int
    report_version_id: int
    comment_text: str
    created_at: datetime

class CommentUpdate(BaseModel):
    comment_text: str