from typing import Annotated, List
from fastapi import APIRouter, Depends, Form, HTTPException
import json
from datetime import datetime
from controller.utils.current_user import get_current_user
from sqlalchemy.orm import Session
from database import get_db
from models.users import User
import os
from models.notification import New_notification
from models.roleReview import RoleReview,CoreFocusArea,CriticalActivities
from routes.report.schema.report_schema import ReportResponse,ReportContentResponse,ReportCreate,ReportVersionResponse,ManagerResponse,NotificationResponse
from models.report import Report,ReportVersion,ReportContent
from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
import boto3
from botocore.exceptions import NoCredentialsError

router = APIRouter()


UserDependency = Annotated[dict, Depends(get_current_user)]


@router.get("/notifications/", response_model=List[NotificationResponse])
def get_notifications(current_user:UserDependency, db: Session = Depends(get_db)):
    # Fetch the user and their role
    user_id=None
    if current_user["id"]:
        user_id=current_user["id"]
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    notifications = (
            db.query(New_notification)
            .filter(
                New_notification.user_id == user_id,  # Employee-specific notifications
                New_notification.is_read == False
            )
            .all()
        )
    

    return notifications


@router.put("/notifications/{notification_id}/mark-read/")
def mark_notification_as_read(current_user:UserDependency,
    notification_id: int, 
    # Add role to check if the user or manager is making the request
    db: Session = Depends(get_db)
):
    notification = db.query(New_notification).filter(New_notification.id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    notification.is_read=True
    db.commit()
    return {"message": "Notification marked as read"}

@router.get("/notifications/manager/", response_model=List[NotificationResponse])
def get_notifications_by_manager(current_user:UserDependency, db: Session = Depends(get_db)):
    # Fetch all users under the manager
    manager_id=None
    if current_user["manager_id"]:
        manager_id=current_user["manager_id"]

    users = db.query(User).filter(User.manager_id == manager_id).all()
    user_ids = [user.id for user in users]
    
    # Fetch notifications for these users
    notifications = (
        db.query(New_notification)
        .filter(New_notification.manager_id==manager_id, New_notification.is_read == False)
        .all()
    )
    return notifications

# @router.get("/notifications/manager/{manager_id}", response_model=List[NotificationResponse])
# def get_notifications_by_manager(manager_id: int, db: Session = Depends(get_db)):
#     # Fetch all users under the manager
#     users = db.query(User).filter(User.manager_id == manager_id).all()
#     user_ids = [user.id for user in users]
    
#     # Fetch notifications for these users
#     notifications = (
#         db.query(Notification)
#         .filter(Notification.user_id.in_(user_ids), Notification.is_read == False)
#         .order_by(Notification.created_at.desc())
#         .all()
#     )
#     return notifications


@router.put("/reports/{report_id}/versions", response_model=ReportVersionResponse)
def create_report_version(current_user:UserDependency,report_id: int, db: Session = Depends(get_db)):
    # Get the last version of the report
    last_version = db.query(ReportVersion).filter(ReportVersion.report_id == report_id).order_by(ReportVersion.version_number.desc()).first()

    new_version_number = last_version.version_number + 1 if last_version else 1
    new_pdf_path = f"report_{report_id}_v{new_version_number}.pdf"  # Example PDF path

    new_version = ReportVersion(
        report_id=report_id,
        version_number=new_version_number,
        pdf_path=new_pdf_path
    )

    db.add(new_version)
    db.commit()
    db.refresh(new_version)

    return new_version

@router.get("/reports/{user_id}", response_model=ReportResponse)
def get_report(current_user:UserDependency,user_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.user_id == user_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.get("/users/{user_id}/manager", response_model=ManagerResponse)
def get_manager_by_user_id(current_user:UserDependency,user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user or not user.manager_id:
        raise HTTPException(status_code=404, detail="Manager not found")
    return ManagerResponse(manager_id=user.manager_id)


@router.get("/reports/{user_id}/versions/{version_number}", response_model=ReportContentResponse)
def get_report_content_by_version(current_user:UserDependency,
    user_id: int,
    version_number: int,
    db: Session = Depends(get_db)
):
    # Fetch the report for the given user_id
    report = db.query(Report).filter(Report.user_id == user_id).first()

    if not report:
        raise HTTPException(status_code=404, detail="Report not found for the user")

    # Fetch the specific version for the report
    report_version = (
        db.query(ReportVersion)
        .filter(
            ReportVersion.report_id == report.id,
            ReportVersion.version_number == version_number
        )
        .first()
    )

    if not report_version:
        raise HTTPException(status_code=404, detail="Version not found for the report")

    # Fetch the content for the specific version
    report_content = (
        db.query(ReportContent)
        .filter(ReportContent.report_version_id == report_version.id)
        .first()
    )

    if not report_content:
        raise HTTPException(status_code=404, detail="Content not found for the version")

    # Deserialize JSON content directly from the database
    content = json.loads(report_content.content)

    # Return the content as is
    return {
        "user_id": user_id,
        "version_number": version_number,
        "content": content
    }

# @router.post("/reports", response_model=ReportResponse)
# def create_report(user_id: int = Form(...),manager_id: int = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
#     # Ensure upload directory exists
#     os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#     # Save uploaded file to the uploads folder
#     pdf_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
#     pdf_path = os.path.join(UPLOAD_FOLDER, pdf_filename)
#     with open(pdf_path, "wb") as f:
#         f.write(file.file.read())
#     print(f"File saved at: {pdf_path}")

#     # Fetch the existing report for the user if it exists
#     existing_report = db.query(Report).filter(Report.user_id == user_id).first()

#     if existing_report:
#         # Increment the version number for the existing report
#         last_version = (
#             db.query(ReportVersion)
#             .filter(ReportVersion.report_id == existing_report.id)
#             .order_by(ReportVersion.version_number.desc())
#             .first()
#         )
#         new_version_number = (last_version.version_number + 1) if last_version else 1

#         # Create a new version
#         new_version = ReportVersion(
#             report_id=existing_report.id,
#             version_number=new_version_number,
#             pdf_path=pdf_path  # Use the stored path
#         )
#         db.add(new_version)
#         db.commit()
#         db.refresh(new_version)

#         # Update the report's current version
#         existing_report.current_version_id = new_version.id
#         db.commit()
#     else:
#         # Create a new report if none exists
#         new_report = Report(
#             user_id=user_id,
#             manager_id=manager_id,
#         )
#         db.add(new_report)
#         db.commit()
#         db.refresh(new_report)

#         # Generate the first version
#         new_version = ReportVersion(
#             report_id=new_report.id,
#             version_number=1,
#             pdf_path=pdf_path  # Use the stored path
#         )
#         db.add(new_version)
#         db.commit()
#         db.refresh(new_version)

#         # Update the current version ID in the report
#         new_report.current_version_id = new_version.id
#         db.commit()
#         existing_report = new_report  # For consistency in variable naming

#     return existing_report


# UPLOAD_FOLDER = "./uploads"
# from dotenv import load_dotenv
# S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
# S3_REGION =os.getenv('S3_REGION') # change to your region
# S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
# S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')

S3_BUCKET_NAME = "activate-pdfstorage"
S3_REGION = "ap-southeast-2"  # change to your region
S3_ACCESS_KEY = "AKIAU6GDWWBFXN3GGZOV"
S3_SECRET_KEY="/c2cN1w7xeBYxgHbUNH1/8FPpjVGSYTbMdyhBmnW"


# Initialize boto3 S3 client
s3_client = boto3.client('s3', 
                         aws_access_key_id=S3_ACCESS_KEY,
                         aws_secret_access_key=S3_SECRET_KEY,
                         region_name=S3_REGION)  # Define your upload folder path

@router.post("/reports", response_model=ReportResponse)
def create_report(current_user:UserDependency,user_id: int = Form(...),manager_id: int = Form(...), role: str = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Ensure upload directory exists
    # os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    if role not in ["employee", "manager"]:
        raise HTTPException(status_code=400, detail="Invalid role. It must be either 'user' or 'manager'.")


    # Save uploaded file to the uploads folder
    pdf_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    

    # Upload the file to S3
    try:
        s3_client.upload_fileobj(file.file, S3_BUCKET_NAME, pdf_filename,ExtraArgs={
            "ACL": "public-read",
            "ContentDisposition": f"inline; filename={pdf_filename}"  # For inline viewing with filename
        })
        pdf_url = f"https://{S3_BUCKET_NAME}.s3.{S3_REGION}.amazonaws.com/{pdf_filename}"
    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="AWS credentials not available.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # pdf_path = os.path.join(UPLOAD_FOLDER, pdf_filename)
    # with open(pdf_path, "wb") as f:
    #     f.write(file.file.read())
    print(f"File uploaded to: {pdf_url}")

    # Fetch the existing report for the user if it exists
    existing_report = db.query(Report).filter(Report.user_id == user_id).first()

    if existing_report:
        existing_versions_count = db.query(ReportVersion).filter(ReportVersion.report_id == existing_report.id).count()

        if existing_versions_count >= 4:
            # raise HTTPException(
            #     status_code=400,
            #     detail="You can only have up to 3 versions of a report. Please subscribe for additional versions."
            # )
            return ReportResponse(
                id=existing_report.id,
                user_id=existing_report.user_id,
                manager_id=existing_report.manager_id,
                current_version_id=existing_report.current_version_id,
                created_at=existing_report.created_at,
                updated_at=existing_report.updated_at,
                detail="You can only have up to 3 versions of a report. Please subscribe for additional versions."
            )
        # Increment the version number for the existing report
        last_version = (
            db.query(ReportVersion)
            .filter(ReportVersion.report_id == existing_report.id)
            .order_by(ReportVersion.version_number.desc())
            .first()
        )
        new_version_number = (last_version.version_number + 1) if last_version else 1
        print("pdf_url",pdf_url)
        # Create a new version
        new_version = ReportVersion(
            report_id=existing_report.id,
            version_number=new_version_number,
            pdf_path=pdf_url,
            # manager_comments=comment  # Use the stored path
        )
        db.add(new_version)
        db.commit()
        db.refresh(new_version)

        # Update the report's current version
        existing_report.current_version_id = new_version.id
        db.commit()
        create_report_notification(existing_report, role, is_new_version=True,db=db)
    else:
        print("pdf_url",pdf_url)
        # Create a new report if none exists
        new_report = Report(
            user_id=user_id,
            manager_id=manager_id,
            pdf_path=pdf_url,
            role=role,
            # manager_comments=comment
        )
        db.add(new_report)
        db.commit()
        db.refresh(new_report)

        # Generate the first version
        new_version = ReportVersion(
            report_id=new_report.id,
            version_number=1,
            pdf_path=pdf_url ,
              # Use the stored path
        )
        db.add(new_version)
        db.commit()
        db.refresh(new_version)

        # Update the current version ID in the report
        new_report.current_version_id = new_version.id
        db.commit()
        create_report_notification(new_report, role, is_new_version=False,db=db)
        existing_report = new_report
        print(existing_report)  # For consistency in variable naming
    role_review = db.query(RoleReview).filter(RoleReview.user_id == user_id).first()
    core_focus_areas = db.query(CoreFocusArea).filter(CoreFocusArea.user_id == user_id).all()
    critical_activities = db.query(CriticalActivities).filter(CriticalActivities.user_id == user_id).all()

    # Structure the content
    report_content_data = {}

    # Include RoleReview data
    if role_review:
        report_content_data['role_review'] = {
            'name': role_review.name,
            'purpose': role_review.purpose,
            'title': role_review.title,
            'organization': role_review.organization,
            'date': role_review.date.isoformat(),
            'prepared_by': role_review.prepared_by,
            'job_summary': role_review.job_summary
        }

    # Include CoreFocusArea data with nested CriticalActivities
    if core_focus_areas:
        focus_area_map = {focus_area.id: focus_area for focus_area in core_focus_areas}
        critical_activities_map = {}
        
        for activity in critical_activities:
            critical_activities_map.setdefault(activity.core_focus_area_id, []).append({
                'area': activity.area,
                'importance': activity.importance
            })

        report_content_data['core_focus_areas'] = [
            {
                'area': focus_area.area,
                'time_spent': focus_area.time_spent,
                'importance': focus_area.importance,
                'critical_activities': critical_activities_map.get(focus_area.id, [])
            }
            for focus_area in core_focus_areas
        ]
    print("report_content_data",report_content_data)

    # Add new content for the version
    report_content = ReportContent(
        report_version_id=new_version.id,
        content=json.dumps(report_content_data)
    )
    db.add(report_content)
    db.commit()
    db.refresh(report_content)

    return ReportResponse(
                id=existing_report.id,
                user_id=existing_report.user_id,
                manager_id=existing_report.manager_id,
                current_version_id=existing_report.current_version_id,
                created_at=existing_report.created_at,
                updated_at=existing_report.updated_at,
                detail="Report is created successfully"
            )

def create_report_notification(report, role, is_new_version,db):
    # Determine who created the report or version based on role
    if is_new_version:
        # Fetch the latest report version
        current_version = db.query(ReportVersion).filter(ReportVersion.id == report.current_version_id).first()
        
        if not current_version:
            raise HTTPException(status_code=404, detail="Current report version not found")

        version_message = f"to version {current_version.version_number}"
        user = db.query(User).filter(User.id == report.user_id).first()
        if role == "manager":
            
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            message = f"Manager updated {user.name}'s report {version_message}."
            notification = New_notification(
                user_id=report.user_id,
                message=message,
                is_read=False,
                
                created_at=datetime.now(),
                # manager_id=report.manager_id if report.manager_id else None
            )
            
            # message = f"Manager updated your report {version_message}."
        else:  # If the user is creating or updating the report
            message = f"{user.name}'s report has been updated {version_message}."
            notification = New_notification(
                # user_id=report.user_id,
                message=message,
                is_read=False,
                
                created_at=datetime.now(),
                manager_id=user.manager_id
            )
    else:
        user = db.query(User).filter(User.id == report.user_id).first()
        # If the report is being created and no version update
        if role == "manager":
            message = f"Manager created {user.name}'s report successfully."
        else:  # If the user created the report
            message = f"{user.name}'s report has been created successfully."

    # Create the notification
    
    # notification = Notification(
    #     user_id=report.user_id,
    #     message=message,
    #     is_read_by_user=False,
    #     is_read_by_manager=False,
    #     created_at=datetime.now(),
    #     manager_id=report.manager_id if report.manager_id else None
    # )
    # db.add(notification)
    # db.commit()




@router.get("/reports/{user_id}/versions", response_model=List[ReportVersionResponse])
def get_report_versions(current_user:UserDependency,
    user_id: int,
    db: Session = Depends(get_db)
):
    # Fetch reports for the given user_id
    reports = db.query(Report).filter(Report.user_id == user_id).all()

    if not reports:
        raise HTTPException(status_code=404, detail="Reports not found for the user")

    # Fetch versions for each report
    report_versions = []
    for report in reports:
        versions = db.query(ReportVersion).filter(ReportVersion.report_id == report.id).all()
        for version in versions:
            # Remove redundant `uploads/` prefix if it exists
            clean_path = version.pdf_path.lstrip('./')
            version.pdf_path = f"http://localhost:8000/{clean_path}"  # Ensure single `uploads/`
        report_versions.extend(versions)

    if not report_versions:
        raise HTTPException(status_code=404, detail="Versions not found for the reports")

    return report_versions




# @router.get("/reports/{user_id}/versions", response_model=List[ReportVersionResponse])
# def get_report_versions(
#     user_id: int,
#     db: Session = Depends(get_db)
# ):
#     # Fetch reports for the given user_id
#     reports = db.query(Report).filter(Report.user_id == user_id).all()

#     if not reports:
#         raise HTTPException(status_code=404, detail="Reports not found for the user")

#     # Fetch versions for each report
#     report_versions = []
#     for report in reports:
#         versions = db.query(ReportVersion).filter(ReportVersion.report_id == report.id).all()
#         report_versions.extend(versions)

#     if not report_versions:
#         raise HTTPException(status_code=404, detail="Versions not found for the reports")

#     return report_versions
