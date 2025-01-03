from fastapi import APIRouter, HTTPException, Depends
from controller.utils.current_user import get_current_user
from models.emailQueue import EmailQueue
from models.report import Report, ReportContent, ReportVersion
from routes.history_routes.schema.history_schema import ReportVersionContentResponse
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime
import json
from typing import Annotated, List


router = APIRouter()


UserDependency = Annotated[dict, Depends(get_current_user)]
# Get a database session


# @router.get("/report_history/{user_id}/versions", response_model=List[ReportVersionContentResponse])
# def get_all_versions_content(
#     user_id: int,
#     db: Session = Depends(get_db)
# ):
#     # Fetch the report for the given user_id
#     report = db.query(Report).filter(Report.user_id == user_id).first()

#     if not report:
#         raise HTTPException(status_code=404, detail="Report not found for the user")

#     # Fetch all versions for the report
#     report_versions = db.query(ReportVersion).filter(ReportVersion.report_id == report.id).all()

#     if not report_versions:
#         raise HTTPException(status_code=404, detail="No versions found for the report")

#     response_data = []
    
#     # Iterate through each version and fetch the associated content
#     for version in report_versions:
#         report_content = db.query(ReportContent).filter(ReportContent.report_version_id == version.id).first()

#         if report_content:
#             content_data = json.loads(report_content.content)
#         else:
#             content_data = {}

#         # Add the version number and associated content to the response
#         response_data.append({
#             "version_number": version.version_number,
#             "content": content_data
#         })

#     # Return the response with versioned contents
#     return response_data
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import json
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Define Pydantic models for response
class ReportVersionContentResponse(BaseModel):
    version_number: int
    content: dict

class EmailHistoryResponse(BaseModel):
    subject: str
    body: str
    status: str
    sent_at: str | None

class ReportHistoryResponse(BaseModel):
    report_history: List[ReportVersionContentResponse]
    email_history: List[EmailHistoryResponse]

# Endpoint to fetch report versions and email history
@router.get("/report_history/{user_id}/versions", response_model=ReportHistoryResponse)
def get_all_versions_content(current_user:UserDependency,
    user_id: int,
    db: Session = Depends(get_db)
):
    # Fetch the report for the given user_id
    report = db.query(Report).filter(Report.user_id == user_id).first()

    if not report:
        raise HTTPException(status_code=404, detail="Report not found for the user")

    # Fetch all versions for the report
    report_versions = db.query(ReportVersion).filter(ReportVersion.report_id == report.id).all()

    if not report_versions:
        raise HTTPException(status_code=404, detail="No versions found for the report")

    response_data = []

    # Iterate through each version and fetch the associated content
    for version in report_versions:
        report_content = db.query(ReportContent).filter(ReportContent.report_version_id == version.id).first()

        if report_content:
            content_data = json.loads(report_content.content)
        else:
            content_data = {}

        # Add the version number and associated content to the response
        response_data.append(ReportVersionContentResponse(
            version_number=version.version_number,
            content=content_data
        ))

    # Fetch email history for the user
    email_history = db.query(EmailQueue).filter(
        (EmailQueue.recipient_id == user_id)
        & (EmailQueue.recipient_type == "user")
    ).all()

    email_history_data = [
        EmailHistoryResponse(
            subject=email.subject,
            body=email.body,
            status=email.status,
            sent_at=email.sent_at.isoformat() if email.sent_at else None
        ) for email in email_history
    ]

    return ReportHistoryResponse(
        report_history=response_data,
        email_history=email_history_data
    )
