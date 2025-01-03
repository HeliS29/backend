from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from controller.utils.current_user import get_current_user
from controller.utils.email_request import send_email_via_smtp
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db
from models.emailQueue import EmailQueue
from models.notification import Notification
from models.users import User
from models.profile import Manager
from models.report import ReportVersion,Report
from routes.emailRequest.schema.email_schema import EmailRequest

router = APIRouter()


UserDependency = Annotated[dict, Depends(get_current_user)]

def notify_user(user_id, message, db):
    from datetime import datetime

    new_notification = Notification(
        user_id=user_id,
        message=message,
        created_at=datetime.now()
    )
    
    db.add(new_notification)
    db.commit()

    return new_notification

# @router.post("/send-email")
# def send_email(request: EmailRequest, db: Session = Depends(get_db)):
#     # Fetch user and manager email
#     user = db.query(User).filter(User.id == request.recipient_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     recipient_email = user.email

#     manager = db.query(Manager).filter(Manager.id == user.manager_id).first()
#     if not manager:
#         raise HTTPException(status_code=404, detail="Manager not found")

#     manager_email = manager.email

#     # Define roadmap email
#     roadmap_email = "helikrish29@gmail.com"

#     new_email = EmailQueue(
#         recipient_id=request.recipient_id,
#         recipient_type=request.recipient_type,
#         subject=request.subject,
#         body=request.body,
#         sent_at=request.sent_at,
#     )
#     db.add(new_email)
#     db.commit()
#     db.refresh(new_email)

#     # Send email using SMTP
#     sent_to_manager = send_email_via_smtp(manager_email, new_email.subject, new_email.body,request.attachment_path)
#     sent_to_user = send_email_via_smtp(recipient_email, new_email.subject, new_email.body,request.attachment_path)
#     sent_to_roadmap = send_email_via_smtp(roadmap_email, new_email.subject, new_email.body,request.attachment_path)

#     if sent_to_manager and sent_to_user and sent_to_roadmap:
#         new_email.status = "sent"
#         new_email.sent_at = datetime.now()
#         db.commit()

#         # Create notifications
#         # message_to_manager = f"Your Role Review report has been sent to {recipient_email}."
#         # notify_user(manager.id, message_to_manager, db)

#         # message_to_user = f"Your Role Review report has been sent."
#         # notify_user(new_email.recipient_id, message_to_user, db)

#         # message_to_roadmap = f"Role Review report sent to {recipient_email} and {manager_email}."
#         # notify_user(None, message_to_roadmap, db)  # Assuming no user_id needed for roadmap notification
#     else:
#         new_email.status = "failed"
#         db.commit()

#     return new_email



@router.post("/send-email")
def send_email(current_user:UserDependency,request: EmailRequest, db: Session = Depends(get_db)):
    # Fetch user and manager email
    user = db.query(User).filter(User.id == request.recipient_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    recipient_email = user.email

    manager = db.query(Manager).filter(Manager.id == user.manager_id).first()
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    manager_email = manager.email

    # Fetch the latest report version for the user
    report_version = (
        db.query(ReportVersion)
        .join(Report, Report.id == ReportVersion.report_id)
        .filter(Report.user_id == request.recipient_id)
        .order_by(ReportVersion.version_number.desc())
        .first()
    )
    if not report_version:
        raise HTTPException(status_code=404, detail="No report version found for the user")

    # Get the path to the PDF
    attachment_path = report_version.pdf_path
    

    new_email = EmailQueue(
        recipient_id=request.recipient_id,
        recipient_type=request.recipient_type,
        subject=request.subject,
        body=request.body,
        sent_at=request.sent_at,
    )
    db.add(new_email)
    db.commit()
    db.refresh(new_email)
    attachment_path = report_version.pdf_path

    # Send email using SMTP
    sent_to_manager = send_email_via_smtp(manager_email, new_email.subject, new_email.body, attachment_path)
    sent_to_user = send_email_via_smtp(recipient_email, new_email.subject, new_email.body, attachment_path)
    sent_to_roadmap = send_email_via_smtp("helikrish29@gmail.com", new_email.subject, new_email.body, attachment_path)

    if sent_to_roadmap:
        new_email.status = "sent"
        new_email.sent_at = datetime.now()
        db.commit()
    else:
        new_email.status = "failed"
        db.commit()

    return new_email
