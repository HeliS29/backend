from typing import Annotated, List
from sqlalchemy.orm import Session
from models.comments import Comment
from routes.comments.schema.comment_schema import CommentCreate,CommentResponse,CommentUpdate
from fastapi import APIRouter, Depends, HTTPException
from controller.utils.email_request import send_email_via_smtp
from models.users import User
from controller.utils.current_user import get_current_user
from datetime import datetime
from database import get_db

router = APIRouter()


UserDependency = Annotated[dict, Depends(get_current_user)]
def create_comment_in_db(db: Session, user_id: int, report_version_id: int, comment_text: str):
    
    db_comment = Comment(
        user_id=user_id,
        report_version_id=report_version_id,
        comment_text=comment_text
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_by_user_id(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Comment).filter(Comment.user_id == user_id).offset(skip).limit(limit).all()

def update_comment_in_db(db: Session, user_id: int, report_version_id: int, comment_text: str):
    db_comment = db.query(Comment).filter(
        Comment.user_id == user_id,
        Comment.report_version_id == report_version_id
    ).first()
    if not db_comment:
        return None
    db_comment.comment_text = comment_text
    db.commit()
    db.refresh(db_comment)
    return db_comment


def update_new_comment_in_db(db: Session, user_id: int,id: int, comment_text: str):
    db_comment = db.query(Comment).filter(
        Comment.user_id == user_id,
        Comment.id == id
    ).first()
    print(f"Querying for user_id={user_id}, comment_id={id}")

    if not db_comment:
        return None
    db_comment.comment_text = comment_text
    db.commit()
    db.refresh(db_comment)
    return db_comment





@router.post("/comments/", response_model=CommentResponse)
def create_comment(current_user:UserDependency,comment: CommentCreate, db: Session = Depends(get_db)):
    print(comment)
    print(f"Received comment: {comment}")
    if not comment.comment_text or comment.comment_text.strip() == "":
        raise HTTPException(status_code=400, detail="Comment content cannot be empty")

    # if not comment.comment_text or comment.comment_text.strip() == "":
    #     print("hello")
    #     raise HTTPException(status_code=400, detail="Comment content cannot be empty")
    return create_comment_in_db(
        db=db,
        user_id=comment.user_id,  # Use the current user's ID
        report_version_id=comment.report_version_id,
        comment_text=comment.comment_text
    )


# Get comments by user_id route
@router.get("/comments/{user_id}", response_model=List[CommentResponse])
def get_comments(current_user:UserDependency,user_id: int, db: Session = Depends(get_db)):
    comments = get_comments_by_user_id(db=db, user_id=user_id)
    if not comments:
        return []  # Return an empty list if no comments are found
    return comments


@router.put("/new/comments/{user_id}/{id}", response_model=CommentResponse)
def update_comment(current_user:UserDependency,
    comment_update: CommentUpdate,
    user_id: int,
    id: int,
    db: Session = Depends(get_db)
):
    print(f"Querying for user_id={user_id}, comment_id={id}")
    print(f"Received comment: {comment_update}")
    if not comment_update.comment_text or comment_update.comment_text.strip() == "":
        print("hello")
        raise HTTPException(status_code=400, detail="Comment content cannot be empty")

    updated_comment = update_new_comment_in_db(
        db=db,
        user_id=user_id,
        id=id,
        comment_text=comment_update.comment_text
    )
    if not updated_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return updated_comment


