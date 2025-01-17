from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from models.users import User
from models.profile import *
from routes.profile.schemas.profile_schema import EmployeeCreate,EmployeeCreateresponse,EmployeeResponseForUpdate,EmployeeResponse,ManagerResponse,OrganizationResponse,ManagerCreate,OrganizationCreate
from controller.utils.current_user import get_current_user
router = APIRouter()

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
        "company_name": employee.company_name if employee.company_name is not None else None,
        "manager_id": employee.manager_id if employee.manager_id is not None else None,
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
@router.get("/current-user/{user_id}")
def get_current_user_info(user_id:int, db: Session = Depends(get_db),current_user: dict = Depends(get_current_user)):
    # Use the current_user['id'] to fetch the user from the database
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "name": user.name,  # Fetch name from the users table
        "email": user.email ,
        "job_title": user.job_title ,
        "company_name": user.company_name,
        "purpose": user.purpose,
       
         # Fetch email from the users table
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
@router.post("/add/managers", response_model=ManagerResponse)
def create_manager(current_user:UserDependency,manager: ManagerCreate, db: Session = Depends(get_db)):
    # Check if manager with the same email already exists
    existing_manager = db.query(Manager).filter(Manager.email == manager.email).first()
    if existing_manager:
        raise HTTPException(status_code=400, detail="Manager with this email already exists")
    
    # Create a new manager
    new_manager = Manager(**manager.dict())
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)
    
    return new_manager


# POST API for creating an organization
@router.post("/add/organizations", response_model=OrganizationResponse)
def create_organization(current_user:UserDependency,organization: OrganizationCreate, db: Session = Depends(get_db)):
    # Check if organization with the same name already exists
    existing_organization = db.query(Organization).filter(Organization.name == organization.name).first()
    if existing_organization:
        raise HTTPException(status_code=400, detail="Organization with this name already exists")
    
    # Create a new organization
    new_organization = Organization(**organization.dict())
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)
    
    return new_organization
