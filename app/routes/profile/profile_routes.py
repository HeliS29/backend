
from smtplib import SMTP
from typing import Annotated, List
from fastapi import APIRouter, Body, Depends, HTTPException,status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from models.emailQueue import EmailQueue
from controller.auth import create_jwt_token, verify_jwt_token
from routes.emailRequest.emailRequest import send_email
from routes.auth.schemas.auth_schema import UserResponse
from sqlalchemy.orm import Session
from database import get_db
from models.users import User, UserRole
from passlib.context import CryptContext
from models.profile import *
from routes.profile.schemas.profile_schema import CurrentUserInfoResponse, EmployeeCreate,EmployeeCreateresponse,EmployeeResponseForUpdate,EmployeeResponse, LinkRegistrationResponse,ManagerResponse, NewEmployeeCreate, NewEmployeeResponse, OrganizationNameResponse,OrganizationResponse,ManagerCreate,OrganizationCreate, RegistrationReq, ResendEmail, resendEmailResponse, updateDetails
from controller.utils.current_user import get_current_user
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
UserDependency = Annotated[dict, Depends(get_current_user)]
# @router.get("/employee/profile/", response_model=EmployeeResponse)
# def get_employee_profile(current_user: UserDependency, db: Session = Depends(get_db)):
#     print(current_user)
#     user_id = current_user['id']
#     employee = db.query(User).filter(User.id == user_id).first()
#     # employee = db.query(Employee, User.name).join(User).filter(Employee.id == employee_id).first()
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     user_name = db.query(User.name).filter(User.id == employee.id).first()
#     if not user_name:
#         raise HTTPException(status_code=404, detail="User not found")

#     return {
#         "user_id": employee.id,
#         "name": user_name[0],  # Assuming user_name is a tuple (name,)
#         "manager_id": employee.manager_id if employee.manager_id is not None else None,
#         "job_title": employee.job_title if employee.job_title is not None else None,
#         "organization_id": employee.organization_id if employee.organization_id is not None else None,
#         "created_at": employee.created_at,
#         "updated_at": employee.updated_at
#     }
@router.get("/employee/profile/", response_model=EmployeeResponseForUpdate)
def get_employee_profile(current_user: UserDependency, db: Session = Depends(get_db)):
    user_id = current_user['id']
    employee = db.query(User).filter(User.id == user_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "id": employee.id,
        "job_title": employee.job_title if employee.job_title is not None else None,
        # "company_name": employee.company_name if employee.company_name is not None else None,
        # "manager_id": employee.manager_id if employee.manager_id is not None else None,
        "purpose": employee.purpose if employee.purpose is not None else None,
        "updated_at": employee.updated_at,
    }
@router.put("/employee/profile/", response_model=EmployeeResponseForUpdate)
def update_employee_profile(
    current_user: UserDependency,
    updated_data: EmployeeCreate,
    db: Session = Depends(get_db),
):
    user_id = current_user['id']
    employee = db.query(User).filter(User.id == user_id).first()
    print(employee)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Update fields if provided in the request
    if updated_data.job_title is not None:
        employee.job_title = updated_data.job_title
    if updated_data.company_name is not None:
        employee.company_name = updated_data.company_name
    if updated_data.purpose is not None:
        employee.purpose = updated_data.purpose
    if updated_data.manager_id is not None:
        # Validate the manager_id
        manager = db.query(Manager).filter(Manager.id == updated_data.manager_id).first()
        if not manager:
            raise HTTPException(status_code=404, detail="Manager not found")
        employee.manager_id = updated_data.manager_id

    # Commit changes to the database
    db.commit()
    db.refresh(employee)

    return {
        "id": employee.id,
        "job_title": employee.job_title,
        "company_name": employee.company_name,
        "manager_id": employee.manager_id,
        "purpose": employee.purpose,
        "updated_at": employee.updated_at,
    }
# @router.get("/current-user")
# def get_current_user_info(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
#     # Use the current_user['id'] to fetch the user from the database
#     user = db.query(User).filter(User.id == current_user['id']).first()

#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     return {
#         "name": user.name,  # Fetch name from the users table
#         "email": user.email ,
#         "job_title": user.job_title ,
#         "company_name": user.company_name,
#         "purpose": user.purpose,
       
#          # Fetch email from the users table
#     }
@router.get("/current-user/{user_id}", response_model=CurrentUserInfoResponse)
def get_current_user_info(
    user_id: int,
    db: Session = Depends(get_db),
     # Assuming this gives you the current logged-in user
):
    # Fetch the user and their associated organization
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch the organization using the organization_id from the user
    organization = db.query(Organization).filter(Organization.id == user.organization_id).first()

    # Check if the organization exists
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")

    # Fetch the manager using the manager_id from the user
    manager = db.query(Manager).filter(Manager.id == user.manager_id).first()

    # Check if the manager exists
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    # Return user info including the organization name as company_name and manager details
    return {
        "name": user.name,  # User's name
        "email": user.email,  # User's email
        "job_title": user.job_title,  # User's job title
        "company_name": organization.name,  # Organization name as company_name
        "purpose": user.purpose,  # User's purpose
        "manager_name": manager.name,  # Manager's name
        "manager_email": manager.email,  # Manager's email
    }

# @router.put("/employee/profile/", response_model=EmployeeResponseForUpdate)
# def update_employee_profile(current_user: UserDependency, updated_data: EmployeeCreate, db: Session = Depends(get_db)):
#     user_id = current_user['id']
#     employee = db.query(User).filter(User.id == user_id).first()
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found")

#     # Update fields
#     if updated_data.manager_id is not None:
#         employee.manager_id = updated_data.manager_id
#     if updated_data.job_title is not None:
#         employee.job_title = updated_data.job_title
#     if updated_data.organization_id is not None:
#         employee.organization_id = updated_data.organization_id
#     db.commit()
#     db.refresh(employee)
#     return employee


# API Endpoints
@router.get("/managers", response_model=list[ManagerResponse])
def get_managers(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    managers = db.query(Manager).all()
    if not managers:
        raise HTTPException(status_code=404, detail="No managers found")
    return managers


@router.get("/organizations", response_model=list[OrganizationResponse])
def get_organizations(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    organizations = db.query(Organization).all()
    if not organizations:
        raise HTTPException(status_code=404, detail="No organizations found")
    return organizations




# POST API for adding a manager
# @router.post("/add/managers", response_model=ManagerResponse)
# def create_manager(current_user:UserDependency,manager: ManagerCreate, db: Session = Depends(get_db)):
#     # Check if manager with the same email already exists
#     existing_manager = db.query(Manager).filter(Manager.email == manager.email).first()
#     if existing_manager:
#         raise HTTPException(status_code=400, detail="Manager with this email already exists")
    
#     # Create a new manager
#     new_manager = Manager(**manager.dict())
#     db.add(new_manager)
#     db.commit()
#     db.refresh(new_manager)
    
#     return new_manager
  # Adjust imports as needed



# Create manager API
# @router.post("/add/managers", response_model=ManagerResponse)
# def create_manager(current_user: UserDependency, manager: ManagerCreate, db: Session = Depends(get_db)):
#     # Fetch current logged-in user (assumed that current_user is a dependency containing user info)
#     print(current_user)
#     current_user_id = current_user['manager_id']  # Assuming the `UserDependency` includes `id`
    
#     # Fetch the manager associated with the current user
#     current_manager = db.query(Manager).filter(Manager.id == current_user_id).first()
    
#     if not current_manager:
#         raise HTTPException(status_code=404, detail="Manager not found for the current user")
    
#     # Get the organization ID of the current manager
#     organization_id = current_manager.organization_id

#     # Check if the organization exists
#     organization = db.query(Organization).filter(Organization.id == organization_id).first()
#     if not organization:
#         raise HTTPException(status_code=404, detail="Organization not found")

#     # Check if manager with the same email already exists in the same organization
#     existing_manager = db.query(Manager).filter(Manager.email == manager.email, Manager.organization_id == organization_id).first()
#     if existing_manager:
#         raise JSONResponse(status_code=400, detail="Manager with this email already exists in this organization")

#     # Create the new manager in the Manager table
#     new_manager = Manager(
#         name=manager.name,
#         email=manager.email,
#         organization_id=organization_id, 
#          # Associate with current manager's organization
#     )
#     db.add(new_manager)
#     db.commit()
#     db.refresh(new_manager)

#     # Now create the manager in the User table
#     user_role = db.query(UserRole).filter(UserRole.role == 'manager').first()
#     if not user_role:
#         raise HTTPException(status_code=404, detail="Manager role not found")
    
#     # Generate a temporary password for the manager (can also be customized or provided by the user)
#      # This should be a secure random password
#     hashed_password = pwd_context.hash(manager.password)
    
#     # Create a new user associated with the manager
#     new_user = User(
#         name=manager.name,
#         email=manager.email,
#         password_hash=hashed_password,  # Hash the password before saving in production
#         role_id=user_role.id,
#         job_title=manager.job_title,
#         organization_id=organization_id,
#         manager_id=current_user_id,  # Associate the manager_id with user
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     # Send the email with login credentials
#     send_manager_email(manager.email, manager.name, manager.password)

#     # Return the created manager
#     return new_manager
# ----------------------------------------------New-------------------------------
@router.post("/add/managers", response_model=ManagerResponse)
def create_manager(current_user: UserDependency, manager: ManagerCreate, db: Session = Depends(get_db)):
    # Fetch current logged-in user (assumed that current_user is a dependency containing user info)
    print(current_user)
    current_user_id = current_user['manager_id']  # Assuming the `UserDependency` includes `id`
    
    # Fetch the manager associated with the current user
    current_manager = db.query(Manager).filter(Manager.id == current_user_id).first()
    
    if not current_manager:
        raise HTTPException(status_code=404, detail="Manager not found for the current user")
    
    # Get the organization ID of the current manager
    organization_id = current_manager.organization_id

    # Check if the organization exists
    organization = db.query(Organization).filter(Organization.id == organization_id).first()
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    # Check if manager with the same email already exists in the same organization
    existing_manager = db.query(Manager).filter(Manager.email == manager.email, Manager.organization_id == organization_id).first()
    if existing_manager:
        return JSONResponse(status_code=400, content={"detail": "Manager with this email already exists in this organization"})

    # Create the new manager in the Manager table
    new_manager = Manager(
        name=manager.name,
        email=manager.email,
        organization_id=organization_id  # Associate with current manager's organization
    )
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)

    # Now create the manager in the User table
    user_role = db.query(UserRole).filter(UserRole.role == 'manager').first()
    if not user_role:
        raise HTTPException(status_code=404, detail="Manager role not found")
    
    # Hash the password before saving
    hashed_password = pwd_context.hash(manager.password)
    
    # Create a new user associated with the manager
    new_user = User(
        name=manager.name,
        email=manager.email,
        password_hash=hashed_password,
        role_id=user_role.id,
        job_title=manager.job_title,
        organization_id=organization_id,
        manager_id=current_user_id,  # Associate the manager_id with user
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Fetch the newly created user's ID
    existing_employee = db.query(User).filter(User.email == manager.email).first()
    if not existing_employee:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate form token
    form_token = create_jwt_token({"user_id": existing_employee.id})
    print("Generated form token:", form_token)

    # Create the form link
    form_link = f"http://activate-hrm.s3-website-ap-southeast-2.amazonaws.com/user_details-stepss/{form_token}"

    # Send the email with login credentials and form link
    send_manager_email(manager.email, manager.name, manager.password, form_link)

    # Return the created manager
    return new_manager

def send_manager_email(manager_email: str, manager_name: str, password: str, form_link: str):
    """Send email with manager's login details."""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    EMAIL_USERNAME = "helishah2116@gmail.com"  # Your Gmail address
    EMAIL_PASSWORD = "lkyr uoby fjql ygka" # Your email app password or SMTP password

    msg = MIMEMultipart()
    msg['From'] = EMAIL_USERNAME
    msg['To'] = manager_email
    msg['Subject'] = "Welcome to Role Review – You have been invited to complete a Role Review Activity"

    body = f"""

    Welcome to Role Review, powered by Activate Human Capital Group!  
    You have been asked to complete a Role Review activity for one of the following purposes:  
    - New Role Design/Development  
    - Onboarding  
    - Performance Management  
    - Succession Planning/Retirement  
    - Delegate & Elevate  

    Please click the link below to begin the process. If needed, there are short videos to guide you:  
    {form_link} 

    Your login details:  
    - **Email:** {manager_email}  
    - **Temporary Password:** {password}   

    The Role Review process was designed to improve clarity of expectations, communications, and the path to career success.  
    Thank you for making this investment of approximately 25 minutes – a little clarity can go a LONG way when it comes to career satisfaction and employee engagement.  

    For additional support or information, please contact info@activatehcg.com.  

    Best regards,  
    Activate Human Capital Group
    """

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {manager_email}")
        # new_email = EmailQueue(
        #     recipient_id=manager_name,  # You can replace this with the actual manager ID if needed
        #     recipient_type="manager",
        #     subject="Your Manager Account Credentials",
        #     body=body,
        #     sent_at=datetime.utcnow()
        # )
        # db.add(new_email)
        # db.commit()
        # db.refresh(new_email)
    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=500, detail="Failed to send email")




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# @router.post("/add/organizations", response_model=OrganizationResponse)
# def create_organization_with_manager(
#     current_user: UserDependency,
#     organization: OrganizationCreate, 
    
#     db: Session = Depends(get_db),
# ):
#     # Check if an organization with the same name already exists
#     existing_organization = db.query(Organization).filter(Organization.name == organization.organization_name).first()
#     if existing_organization:
#         # raise HTTPException(status_code=400, detail="Organization with this name already exists")
#         return JSONResponse(status_code=400, content={"message": "Organization with this name already exists"})

#     # Create a new organization
#     new_organization = Organization(name=organization.organization_name)
#     db.add(new_organization)
#     db.commit()
#     db.refresh(new_organization)

#     # Check if the 'manager' role exists
#     user_role = db.query(UserRole).filter(UserRole.role == 'manager').first()
#     if not user_role:
#         raise HTTPException(status_code=404, detail="Manager role not found")

#     # Check if a manager already exists with the same email in this organization
#     existing_manager = db.query(Manager).filter(Manager.email == organization.manager_email, Manager.organization_id == new_organization.id).first()
#     print("existing_manager",existing_manager)
#     if existing_manager:
#         # raise HTTPException(status_code=400, detail="A manager with this email already exists in the same organization")
#         return JSONResponse(status_code=400, content={"message": "A manager with this email already exists in the same organization"})

#     # Hash the provided manager password
#     hashed_password = pwd_context.hash(organization.manager_password)

#     # Create a manager using the provided details
#     new_manager = Manager(
#         name=organization.manager_name,
#         email=organization.manager_email,
#         organization_id=new_organization.id,
#     )
#     db.add(new_manager)
#     db.commit()
#     db.refresh(new_manager)

#     # Create the manager as a user in the User table
#     new_user = User(
#         name=new_manager.name,
#         email=new_manager.email,
#         password_hash=hashed_password,
#         role_id=user_role.id,
#         organization_id=new_organization.id,
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_organization
# -------------------------New--------------------------------------------------
smtp_server = "smtp.gmail.com"
smtp_port = 587
EMAIL_USERNAME = "helishah2116@gmail.com"  # Your Gmail address
EMAIL_PASSWORD = "lkyr uoby fjql ygka"  # Your email password
 # Sender email

def send_email(recipient_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USERNAME
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

@router.post("/add/organizations", response_model=OrganizationResponse)
def create_organization_with_manager(
    current_user: UserDependency,
    organization: OrganizationCreate, 
    db: Session = Depends(get_db),
):
    # Check if an organization with the same name already exists
    existing_organization = db.query(Organization).filter(Organization.name == organization.organization_name).first()
    if existing_organization:
        return JSONResponse(status_code=400, content={"message": "Organization with this name already exists"})

    # Create a new organization
    new_organization = Organization(name=organization.organization_name)
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)

    # Check if the 'manager' role exists
    user_role = db.query(UserRole).filter(UserRole.role == 'manager').first()
    if not user_role:
        raise HTTPException(status_code=404, detail="Manager role not found")

    # Check if a manager with the same email already exists in this organization
    existing_manager = db.query(Manager).filter(
        Manager.email == organization.manager_email, 
        Manager.organization_id == new_organization.id
    ).first()

    if existing_manager:
        return JSONResponse(status_code=400, content={"message": "A manager with this email already exists in the same organization"})

    # Hash the provided manager password
    hashed_password = pwd_context.hash(organization.manager_password)

    # Create a manager entry
    new_manager = Manager(
        name=organization.manager_name,
        email=organization.manager_email,
        organization_id=new_organization.id,
        is_owner=True
    )
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)

    # Create a user entry for the manager
    new_user = User(
        name=new_manager.name,
        email=new_manager.email,
        password_hash=hashed_password,
        role_id=user_role.id,  # Assign "manager" role
        organization_id=new_organization.id,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    login_link = "http://activate-hrm.s3-website-ap-southeast-2.amazonaws.com/"
    # Send welcome email
    email_subject = "Welcome to Role Review powered by Activate Human Capital Group – You are now the Org Admin"
    email_body = f"""
    Welcome to Role Review, powered by Activate Human Capital Group! 

    You have been set up as your organization’s Admin User to create managers, employees, and assign Role Review efforts for any of the following purposes:

    - New Role Design/Development
    - Onboarding
    - Performance Management
    - Succession Planning/Retirement
    - Delegate & Elevate

    Please save your login and password for future use:
    Login: {login_link} 
    Password: {organization.manager_password}

    For additional support or information, please contact info@activatehcg.com
    """

    send_email(new_user.email, email_subject, email_body)

    return new_organization

@router.get("/organizations/{organization_id}")
def get_organization(organization_id: int, db: Session = Depends(get_db)):
    organization = db.query(Organization).filter(Organization.id == organization_id).first()
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")

    # Fetch the user with role_id = 4 (Owner) for the organization
    owner = (
    db.query(User)
    .filter(
        User.organization_id == organization.id,
        User.role_id == 3,
        User.manager_id == None  # Ensure manager_id is NULL
    )
    .first()
)
    return {
        "organization_name": organization.name,
        "owner_name": owner.name if owner else "N/A",
        "owner_email": owner.email if owner else "N/A",
        "created_at": organization.created_at,
    }

class OrganizationUpdate(BaseModel):
    organization_name: str
    owner_name: str
    owner_email: EmailStr

@router.put("/organizations/{organization_id}")
def update_organization(
    organization_id: int,
    org_update: OrganizationUpdate,
    db: Session = Depends(get_db),
):
    organization = db.query(Organization).filter(Organization.id == organization_id).first()
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")

    # Fetch the user entry (organization owner)
    owner = (
        db.query(User)
        .filter(
            User.organization_id == organization.id,
            User.role_id == 3,  # Assuming '2' is the role ID for Owner/Admin
            User.manager_id == None  
        )
        .first()
    )

    if not owner:
        raise HTTPException(status_code=404, detail="Account owner not found")

    # Fetch the corresponding manager entry for the owner
    owner_manager = (
        db.query(Manager)
        .filter(
            Manager.organization_id == organization.id,
            Manager.is_owner == True  # Ensure we are updating only the owner manager
        )
        .first()
    )

    if not owner_manager:
        raise HTTPException(status_code=404, detail="Owner manager record not found")

    # Update organization details
    organization.name = org_update.organization_name

    # Update the User table
    owner.name = org_update.owner_name
    owner.email = org_update.owner_email

    # Update the Manager table
    owner_manager.name = org_update.owner_name
    owner_manager.email = org_update.owner_email

    db.commit()
    return {"message": "Organization and owner info updated successfully"}


class ResetPassword(BaseModel):
    new_password: str

@router.put("/organizations/{organization_id}/reset-password")
def reset_owner_password(organization_id: int, reset_data: ResetPassword, db: Session = Depends(get_db)):
    owner = db.query(User).filter(User.organization_id == organization_id, User.role_id == 3,User.manager_id == None).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Account owner not found")

    owner.password_hash = pwd_context.hash(reset_data.new_password)
    db.commit()
    
    return {"message": "Password reset successfully"}
# ---------------------------------New----------------------------------------
@router.get("/get-organization-name", response_model=OrganizationNameResponse)
def get_organization_name(current_user:UserDependency, db: Session = Depends(get_db)):
    """
    Get organization name based on manager's id.
    """
    manager_id=current_user['manager_id']
    # Fetch the manager from the database
    manager = db.query(Manager).filter(Manager.id == manager_id).first()
    
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")
    
    # Fetch the associated organization using the organization_id from the manager
    organization = db.query(Organization).filter(Organization.id == manager.organization_id).first()
    
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    return {"organization_name": organization.name}


class GenerateFormLinkResponse(BaseModel):
    registration_url: str
    message: str
    user_id: int
class GenerateFormLinkRequest(BaseModel):
    email: str
@router.post("/generateFormLink", response_model=GenerateFormLinkResponse)
def generate_form_link(
    request: GenerateFormLinkRequest,
    db: Session = Depends(get_db),
):
    # Fetch user from DB using email
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate a JWT token for secure access
    access_token = create_jwt_token({"user_id": user.id})

    # Create the form URL with the token
    form_link = f"http://activate-hrm.s3-website-ap-southeast-2.amazonaws.com/user_details-stepss/{access_token}"

    # Return a structured response
    return {
        "registration_url": form_link,
        "user_id": user.id,
        "message": "Registration link generated successfully"
    }

@router.post("/add/employee", response_model=NewEmployeeResponse)
def create_employee_and_send_email(
    current_manager:UserDependency,  # Current manager dependency
    employee: NewEmployeeCreate,
    db: Session = Depends(get_db),
):
    manager_id = current_manager["manager_id"]

    # Get the manager using the manager_id
    manager = db.query(Manager).filter(Manager.id == manager_id).first()
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")
    # Check if manager exists
   
    # Check if employee already exists
    existing_employee = db.query(User).filter(User.email == employee.email).first()
    if existing_employee:
        # raise HTTPException(status_code=400, detail="Employee with this email already exists")
        return JSONResponse(status_code=400, content={"message": "Employee with this email already exists"})

    # Generate a unique token for the form link
    form_token = create_jwt_token({"email": employee.email})
    print("previopus toke",form_token)
    # Add employee record with status `pending`
    new_employee = User(
        name=employee.name,
        email=employee.email,
        job_title=employee.job_title,
        role_id=db.query(UserRole).filter(UserRole.role == "employee").first().id,
        organization_id=manager.organization_id,
        manager_id=manager.id,
        
         # Mark as pending
          # Store the token for verification
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    # Send email with the form link
    # form_link = f"http://localhost:3001/complete-registration?token={form_token}"
    form_link = f"http://activate-hrm.s3-website-ap-southeast-2.amazonaws.com/complete-registration?token={form_token}"
    
    print(employee.email)
    send_registration_email(employee.name,employee.email,form_token)
    return new_employee
@router.post("/resendEmail/{user_id}", response_model=resendEmailResponse)
def create_employee_and_send_email(
    current_manager:UserDependency,  # Current manager dependency
    user_id:int,
    db: Session = Depends(get_db),
):
    # Get the manager using the manager_id
    
    # Check if manager exists
   
    # Check if employee already exists
    existing_employee = db.query(User).filter(User.id == user_id).first()
    
    # Generate a unique token for the form link
    form_token = create_jwt_token({"user_id": existing_employee.id})
    print("previopus toke",form_token)
    # Add employee record with status `pending`

    # Send email with the form link
   
    form_link = f"http://activate-hrm.s3-website-ap-southeast-2.amazonaws.com/user_details-stepss/{form_token}"
    email_subject = "Welcome to Role Review – You have been invited to complete a Role Review Activity"
    email_body = f"""
    Welcome to Role Review, powered by Activate Human Capital Group!

    You have been asked to complete a Role Review activity for one of the following purposes:

    - New Role Design/Development  
    - Onboarding  
    - Performance Management  
    - Succession Planning/Retirement  
    - Delegate & Elevate  

    Please click the link below to begin the process. If needed, there are short videos to guide you.

    {form_link}

    The Role Review process was designed to improve clarity of expectations, communications, and the path to career success. Thank you for making this investment of approximately 25 minutes – a little clarity can go a LONG way when it comes to career satisfaction and employee engagement.

    For additional support or information, please contact info@activatehcg.com
    """
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    

    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    EMAIL_USERNAME = "helishah2116@gmail.com"  # Your Gmail address
    EMAIL_PASSWORD = "lkyr uoby fjql ygka"  # Your app password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USERNAME
    msg['To'] = existing_employee.email
    msg['Subject'] = email_subject

    # Attach the body
    msg.attach(MIMEText(email_body, 'plain'))

    # Attach the file from the URL if provided
    

    # Sending the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)  # Correct username and password
            server.send_message(msg)
        print(f"Email sent successfully to {existing_employee.email}")
        new_email = EmailQueue(
            recipient_id=existing_employee.id,
            recipient_type="user",
            subject=email_subject,
            body=email_body,
            status="sent", 
            sent_at=datetime.now()
        )
        db.add(new_email)
        db.commit()
        db.refresh(new_email)
        
        return {
            "message": "Email sent successfully",
            "user_id": existing_employee.id,
            "email": existing_employee.email,
            "name": existing_employee.name,
        }
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

    

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def send_registration_email(employee_name: str, employee_email: str,form_token: str,db: Session = Depends(get_db),):
    """Send registration email to the employee."""
    # Construct the form link
    # print("form",form_token)
    # form_link = f"https:/http://localhost:3001/complete-registration?token={form_token}"
    form_link = f"http://activate-hrm.s3-website-ap-southeast-2.amazonaws.com/complete-registration?token={form_token}"
    # Email content
    print(f"Recipient email: {employee_email}")
    email_subject = "Welcome to Role Review – You have been invited to complete a Role Review Activity"
    email_body = f"""
    Welcome to Role Review, powered by Activate Human Capital Group!

    You have been asked to complete a Role Review activity for one of the following purposes:

    - New Role Design/Development  
    - Onboarding  
    - Performance Management  
    - Succession Planning/Retirement  
    - Delegate & Elevate  

    Please click the link below to begin the process. If needed, there are short videos to guide you.

    {form_link}

    The Role Review process was designed to improve clarity of expectations, communications, and the path to career success. Thank you for making this investment of approximately 25 minutes – a little clarity can go a LONG way when it comes to career satisfaction and employee engagement.

    For additional support or information, please contact info@activatehcg.com
    """

    
    # SMTP Configuration (Example for Gmail)
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    

    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    EMAIL_USERNAME = "helishah2116@gmail.com"  # Your Gmail address
    EMAIL_PASSWORD = "lkyr uoby fjql ygka"  # Your app password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USERNAME
    msg['To'] = employee_email
    msg['Subject'] = email_subject

    # Attach the body
    msg.attach(MIMEText(email_body, 'plain'))

    # Attach the file from the URL if provided
    

    # Sending the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)  # Correct username and password
            server.send_message(msg)
        print(f"Email sent successfully to {employee_email}")
        new_email = EmailQueue(
            recipient_id=employee_name,  # You can use employee ID instead if needed
            recipient_type="user",
            subject=email_subject,
            body=email_body,
            status="sent", 
            sent_at=datetime.utcnow()
        )
        db.add(new_email)
        db.commit()
        db.refresh(new_email)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
@router.post("/complete-registration", response_model=LinkRegistrationResponse)
def complete_registration(
    request: RegistrationReq,
    db: Session = Depends(get_db)
):
    # Verify token
    payload = verify_jwt_token(request.token)
    print(payload)
    
   
    
    # Get user data from the payload (assuming payload contains user_id or email)
    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token payload")

    # Fetch the user by user_id (assuming the token contains the user_id)
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Hash password and update user details
    hashed_password = pwd_context.hash(request.password)
    user.password_hash = hashed_password
    # user.job_title = request.job_title if request.job_title else None
    # user.purpose = request.purpose if request.purpose else None
    user.verification_code = None  # Remove token after completion
    user.active = True  # Mark the user as active
    db.commit()

    # Return the response model with a success message
    return LinkRegistrationResponse(message="Registration completed successfully!")
@router.put("/update-user-details", response_model=LinkRegistrationResponse)
def update_user_details(
    request: updateDetails,
    db: Session = Depends(get_db),
):
    # Get user by token (this assumes you pass user_id in the payload)
    payload = verify_jwt_token(request.token)
    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token payload")
    
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update the fields if provided
    user.job_title = request.job_title if request.job_title else user.job_title
    user.purpose = request.purpose if request.purpose else user.purpose
    db.commit()

    return {"message": "User details updated successfully!"}

@router.get("/organizations/{org_id}/managers", response_model=List[ManagerResponse])
def get_managers_by_organization(org_id: int, db: Session = Depends(get_db)):
    # Query to fetch managers for a given organization
    managers = db.query(Manager).filter(Manager.organization_id == org_id).all()
    
    if not managers:
        raise HTTPException(status_code=404, detail="No managers found for this organization")
    
    return managers