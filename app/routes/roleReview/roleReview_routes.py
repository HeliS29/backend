from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from controller.utils.current_user import get_current_user
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db
from models.roleReview import RoleReview
from crud.role_review import (
    create_role_review, 
    get_role_reviews_by_employee, 
    update_role_review   
)
from routes.roleReview.schemas.roleReview_schema import (
    RoleReviewCreate,
    RoleReviewUpdate,
    RoleReviewResponse
)

router = APIRouter()
UserDependency = Annotated[dict, Depends(get_current_user)]


@router.post("/role-review", response_model=RoleReviewResponse)
def create_or_update_review(current_user: UserDependency,role_review: RoleReviewCreate, db: Session = Depends(get_db)):
    # Fetch existing reviews for the user
    if len(role_review.job_summary) > 1000:
        raise HTTPException(
            status_code=400,
            detail="Job summary cannot exceed 1000 characters"
        )
    existing_reviews = get_role_reviews_by_employee(db, role_review.user_id)
    
    if existing_reviews:
        # Assuming only one review needs to be updated
        existing_review = existing_reviews[0]
        
        # Update fields directly
        existing_review.name = role_review.name
        existing_review.title = role_review.title
        existing_review.organization = role_review.organization
        existing_review.prepared_by = role_review.prepared_by
        existing_review.date = datetime.now()
        existing_review.purpose = role_review.purpose
        existing_review.job_summary = role_review.job_summary
        existing_review.updated_at = datetime.now()  # Update the timestamp
        
        # Commit changes to the database
        db.add(existing_review)
        db.commit()
        db.refresh(existing_review)  # Refresh to get updated values from DB
        return existing_review
    else:
        # If no existing review, create a new one
        new_review = RoleReview(
            user_id=role_review.user_id,
            name=role_review.name,
            title=role_review.title,
            organization=role_review.organization,
            date=role_review.date,
            purpose=role_review.purpose,
            prepared_by=role_review.prepared_by,
            job_summary=role_review.job_summary,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        db.add(new_review)
        db.commit()
        db.refresh(new_review)  # Refresh to get ID and other DB-generated values
        return new_review

# Get Role Reviews by Employee ID
@router.get("/role-review/{employee_id}", response_model=list[RoleReviewResponse])
def get_reviews(current_user: UserDependency,employee_id: int, db: Session = Depends(get_db)):
    reviews = get_role_reviews_by_employee(db, employee_id)
    if not reviews:
        raise HTTPException(status_code=404, detail="No role reviews found for this employee")
    return reviews

# Update Role Review
@router.put("/role-review/{user_id}", response_model=RoleReviewResponse)
def update_review(current_user: UserDependency,user_id: int, role_review: RoleReviewUpdate, db: Session = Depends(get_db)):
    updated_review = update_role_review(db, user_id, role_review)
    if not updated_review:
        raise HTTPException(status_code=404, detail="Role review not found")
    return updated_review


