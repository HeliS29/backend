from sqlalchemy.orm import Session
from models.roleReview import *
from routes.roleReview.schemas.roleReview_schema import *
def create_role_review(db: Session, role_review_data: RoleReviewCreate):
    new_review = RoleReview(
        user_id=role_review_data.user_id,
        purpose=role_review_data.purpose,
        name=role_review_data.name,
        title=role_review_data.title,
        organization=role_review_data.organization,
        date=role_review_data.date,
        prepared_by=role_review_data.prepared_by,
        job_summary=role_review_data.job_summary
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


def get_role_reviews_by_employee(db: Session, user_id: int):
    return db.query(RoleReview).filter(RoleReview.user_id == user_id).all()


def update_role_review(db: Session, user_id: int, updated_data: RoleReviewUpdate):
    review = db.query(RoleReview).filter(RoleReview.user_id == user_id).first()
    if review:
        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(review, key, value)
        db.commit()
        db.refresh(review)
        return review
    return None
