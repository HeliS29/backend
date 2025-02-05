from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from models.users import User
from controller.utils.current_user import get_current_user
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db
from models.roleReview import RoleReview, WorkData
from crud.role_review import (
    create_role_review, 
    get_role_reviews_by_employee, 
    update_role_review   
)
from routes.roleReview.schemas.roleReview_schema import (
    RoleReviewCreate,
    RoleReviewUpdate,
    RoleReviewResponse,
    SubmitWorkRequest,
    WorkDataAdd,
    WorkDataWithCommentsResponse
)

router = APIRouter()
UserDependency = Annotated[dict, Depends(get_current_user)]


@router.post("/role-review", response_model=RoleReviewResponse)
def create_or_update_review(role_review: RoleReviewCreate, db: Session = Depends(get_db)):
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
       
        user = db.query(User).filter(User.id == role_review.user_id).first()
        if user:
            user.purpose = role_review.purpose
            user.updated_at = datetime.now()  # Ensure to update the timestamp for the user
            db.add(user)
        
            db.commit()
            db.refresh(user)
        # Commit changes to the database
        db.add(existing_review)
        db.commit()
        db.refresh(existing_review) 
         # Refresh to get updated values from DB
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
        db.refresh(new_review) 
        user = db.query(User).filter(User.id == role_review.user_id).first()
        if user:
            user.purpose = role_review.purpose
            user.updated_at = datetime.now()  # Ensure to update the timestamp for the user
            db.add(user)
        if user:
            db.commit()
            db.refresh(user) # Refresh to get ID and other DB-generated values
        return new_review

# Get Role Reviews by Employee ID
@router.get("/role-review/{employee_id}", response_model=list[RoleReviewResponse])
def get_reviews(employee_id: int, db: Session = Depends(get_db)):
    reviews = get_role_reviews_by_employee(db, employee_id)
    if not reviews:
        raise HTTPException(status_code=404, detail="No role reviews found for this employee")
    return reviews

# Update Role Review
@router.put("/role-review/{user_id}", response_model=RoleReviewResponse)
def update_review(user_id: int, role_review: RoleReviewUpdate, db: Session = Depends(get_db)):
    updated_review = update_role_review(db, user_id, role_review)
    if not updated_review:
        raise HTTPException(status_code=404, detail="Role review not found")
    return updated_review



@router.post('/submit-work', response_model=SubmitWorkRequest)
def submit_work(work_data: SubmitWorkRequest, db: Session = Depends(get_db)):
    try:
        # Delete existing work data for the user
        existing_work_data = db.query(WorkData).filter(WorkData.user_id == work_data.user_id).all()
        for item in existing_work_data:
            db.delete(item)
        db.commit()  # Commit the deletion

        # Validate that the work_data is properly structured
        if not isinstance(work_data.work_data, list):
            raise HTTPException(status_code=400, detail="Work data should be a list")
        
        # Validate that each item has the required fields
        for item in work_data.work_data:
            work_description = item.work_description
            hours_per_month = item.hours_per_month
            rows = item.rows

            if not all([work_description, hours_per_month, rows]):
                raise HTTPException(status_code=400, detail="Missing required fields")

        # Store the data in the database
        work_data_list = []
        for item in work_data.work_data:
            work_data_entry = WorkData(
                user_id=work_data.user_id,
                work_description=item.work_description,
                hours_description=item.hours_per_month,
                rows=item.rows,
                comments=work_data.comments  # Shared comments for all entries for this user
            )
            work_data_list.append(work_data_entry)

        db.add_all(work_data_list)
        db.commit()

        return JSONResponse(content={"message": "Work data submitted successfully"}, status_code=200)

    except Exception as e:
        db.rollback() # Rollback the session if there's an error
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get('/get-work/{user_id}', response_model=WorkDataWithCommentsResponse)
def get_work_data(user_id: int, db: Session = Depends(get_db)):
    try:
        # Fetch the work data for the specific user
        work_data_entries = db.query(WorkData).filter(WorkData.user_id == user_id).all()
        
        if not work_data_entries:
            raise HTTPException(status_code=404, detail="No work data found for the given user")

        # Extract the shared comments (assuming it's the same for all work entries)
        comments = work_data_entries[0].comments  # Assuming the comment is the same for all entries

        # Prepare the response data
        work_data_response = [
            {
                "work_description": entry.work_description,
                "hours_per_month": entry.hours_description,
                
                # Attach the shared comments
            }
            for entry in work_data_entries
        ]

        return WorkDataWithCommentsResponse(
            user_id=user_id,
            work_data=work_data_response,
            comments=comments
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))