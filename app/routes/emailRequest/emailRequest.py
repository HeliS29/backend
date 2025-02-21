import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from controller.utils.current_user import get_current_user
from controller.utils.email_request import send_email_via_smtp
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db
from models.emailQueue import EmailQueue
from models.users import User
from models.profile import Manager
from models.report import ReportVersion,Report
from routes.emailRequest.schema.email_schema import EmailRequest
from apscheduler.schedulers.background import BackgroundScheduler
from database import SessionLocal 
router = APIRouter()


UserDependency = Annotated[dict, Depends(get_current_user)]

# def notify_user(user_id, message, db):
#     from datetime import datetime

#     new_notification = Notification(
#         user_id=user_id,
#         message=message,
#         created_at=datetime.now()
#     )
    
#     db.add(new_notification)
#     db.commit()

#     return new_notification
# s3_bucket_base_url = "https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to send emails
def process_pending_emails():
    db: Session = SessionLocal()
    try:
        logger.info("Running email scheduler...")
        print("Running email scheduler...")

        pending_reports = db.query(ReportVersion).filter(ReportVersion.is_email == False).all()

        for report in pending_reports:
            user = db.query(User).join(Report, Report.id == report.report_id).filter(Report.user_id == User.id).first()
            if not user:
                logger.warning(f"User not found for report ID: {report.id}")
                continue

            recipient_email = user.email
            manager = db.query(Manager).filter(Manager.id == user.manager_id).first()
            if not manager:
                logger.warning(f"Manager not found for report ID: {report.id}")
                continue
            
            manager_email = manager.email
            attachment_path = f"https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/{report.pdf_path}"

            email_body="""
            Please find the attached Role Review Report, powered by Activate Human Capital Group. This activity was completed for one of the following purposes: 
                    New Role Design/Development
                    Onboarding
                    Performance Management
                    Succession Planning/Retirement
                    Delegate & Elevate 
            Next Step: Review this document with your manager to ensure agreement about Core Focus Areas, Priorities, and Activities. The Role Review process was designed to improve clarity of expectations, communications, and the path to career success. Thank you for making this investment of approximately 25 minutes – a little clarity can go a LONG way when it comes to career satisfaction and employee engagement. 
            For additional support or information, please contact info@activatehcg.com
"""

            logger.info(f"Sending email for report ID: {report.id}")
            sent_to_manager = send_email_via_smtp(manager_email, "Completed Role Review – Your Role Review Report is attached", email_body, attachment_path)
            sent_to_user = send_email_via_smtp(recipient_email, "Completed Role Review – Your Role Review Report is attached", email_body, attachment_path)
            sent_to_roadmap = send_email_via_smtp("roadmap@activatehcg.com", "Completed Role Review – Your Role Review Report is attached", email_body, attachment_path)

            if sent_to_manager or sent_to_user or sent_to_roadmap:
                report.is_email = True
                email_record = db.query(EmailQueue).filter(EmailQueue.recipient_id == user.id, EmailQueue.status == "pending").first()
                if email_record:
                    email_record.status = "sent"
                    email_record.sent_at = datetime.now()  # ✅ Mark email as sent
                db.commit()
                logger.info(f"Email sent and updated for report ID: {report.id}")
            else:
                logger.error(f"Failed to send email for report ID: {report.id}")

    except Exception as e:
        logger.error(f"Error in email scheduler: {str(e)}")
    finally:
        db.close()

# Initialize APScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(process_pending_emails, "interval", minutes=5)
scheduler.start()
@router.post("/send-email", response_model=EmailRequest)
def send_email(request: EmailRequest, db: Session = Depends(get_db)):
    try:
        # Fetch user details
        user = db.query(User).filter(User.id == request.recipient_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        recipient_email = user.email

        # Fetch manager details
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

        # Construct the S3 attachment path
        s3_bucket_base_url = "https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com"
        attachment_path = f"{s3_bucket_base_url}/{report_version.pdf_path}" 

        # Send email via SMTP
        email_sent_to_manager = send_email_via_smtp(manager_email, request.subject, request.body, attachment_path)
        email_sent_to_user = send_email_via_smtp(recipient_email, request.subject, request.body, attachment_path)
        email_sent_to_roadmap = send_email_via_smtp("roadmap@activatehcg.com", request.subject, request.body, attachment_path)

        # Determine email status
        email_sent = email_sent_to_manager or email_sent_to_user or email_sent_to_roadmap
        status = "sent" if email_sent else "pending"
        sent_time = datetime.now()

        # Store email record in the database
        new_email = EmailQueue(
            recipient_id=request.recipient_id,
            recipient_type=request.recipient_type,
            subject=request.subject,
            body=request.body,
            status=status,
            created_at=datetime.now(),
            sent_at=sent_time,
        )
        db.add(new_email)
        db.commit()
        db.refresh(new_email)

        return new_email

    except Exception as e:
        logger.error(f"Error while sending email: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    
# -----------mofified change with schedular----------------
# @router.post("/send-email", response_model=EmailRequest)  # ✅ Use Pydantic model for response
# def send_email(request: EmailRequest, db: Session = Depends(get_db)):
#     try:
#     # Here, make sure to pass the necessary parameters.
#     # For example, if your EmailRequest has a recipient_email field:
#         email_sent = send_email_via_smtp(
#             request.recipient_email,  
#             request.subject, 
#             request.body, 
#             request.attachment_path if hasattr(request, "attachment_path") else None
#         )
#     except Exception as e:
#         # Log the error if needed and continue with status "pending"
#         email_sent = False

#     # Set status and sent timestamp based on the result
#     status = "sent" if email_sent else "pending"
#     sent_time = datetime.now() if email_sent else None

#     new_email = EmailQueue(
#         recipient_id=request.recipient_id,
#         recipient_type=request.recipient_type,
#         subject=request.subject,
#         body=request.body,
#         status=status,           # Set status to "sent" if email_sent is True, otherwise "pending"
#         created_at=datetime.now(),
#         sent_at=sent_time,       # Record the sent time if email was successfully sent
#     )
#     db.add(new_email)
#     db.commit()
#     db.refresh(new_email)
#     return new_email
#     # new_email = EmailQueue(
#     #     recipient_id=request.recipient_id,
#     #     recipient_type=request.recipient_type,
#     #     subject=request.subject,
#     #     body=request.body,
#     #     status="pending",  # Default to pending
#     #     created_at=datetime.now(),
#     #     sent_at=request.sent_at,
#     # )
#     # db.add(new_email)
#     # db.commit()
#     # db.refresh(new_email)

#     # return new_email 
# ----------earlier changes-----------------
# @router.post("/send-email")
# def send_email(current_user:UserDependency,request: EmailRequest, db: Session = Depends(get_db)):
#     # Fetch user and manager email
#     user = db.query(User).filter(User.id == request.recipient_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     recipient_email = user.email

#     manager = db.query(Manager).filter(Manager.id == user.manager_id).first()
#     if not manager:
#         raise HTTPException(status_code=404, detail="Manager not found")

#     manager_email = manager.email

#     # Fetch the latest report version for the user
#     report_version = (
#         db.query(ReportVersion)
#         .join(Report, Report.id == ReportVersion.report_id)
#         .filter(Report.user_id == request.recipient_id)
#         .order_by(ReportVersion.version_number.desc())
#         .first()
#     )
#     if not report_version:
#         raise HTTPException(status_code=404, detail="No report version found for the user")

#     # Get the path to the PDF
#     # attachment_path = report_version.pdf_path
    

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
#     # attachment_path = report_version.pdf_path
#     s3_bucket_base_url = "https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com"
#     attachment_path = f"{s3_bucket_base_url}/{report_version.pdf_path}" 

#     # Send email using SMTP
#     sent_to_manager = send_email_via_smtp(manager_email, new_email.subject, new_email.body, attachment_path)
#     sent_to_user = send_email_via_smtp(recipient_email, new_email.subject, new_email.body, attachment_path)
#     sent_to_roadmap = send_email_via_smtp("roadmap@activatehcg.com", new_email.subject, new_email.body, attachment_path)

#     if sent_to_roadmap:
#         new_email.status = "sent"
#         new_email.sent_at = datetime.now()
#         db.commit()
#     elif sent_to_user:
#         new_email.status = "sent"
#         new_email.sent_at = datetime.now()
#         db.commit()
#     elif sent_to_manager:
#         new_email.status = "sent"
#         new_email.sent_at = datetime.now()
#         db.commit()
#     else:
#         new_email.status = "failed"
#         db.commit()

#     return new_email






