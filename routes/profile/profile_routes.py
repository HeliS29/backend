from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from models.users import User
from models.profile import *
from routes.profile.schemas.profile_schema import EmployeeCreate,EmployeeCreateresponse,EmployeeResponseForUpdate,EmployeeResponse,ManagerResponse,OrganizationResponse
from controller.utils.current_user import get_current_user
router = APIRouter()

UserDependency = Annotated[dict, Depends(get_current_user)]
@router.get("/employee/profile/", response_model=EmployeeResponse)
def get_employee_profile(current_user: UserDependency, db: Session = Depends(get_db)):
    print(current_user)
    user_id = current_user['id']
    employee = db.query(User).filter(User.id == user_id).first()
    # employee = db.query(Employee, User.name).join(User).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    user_name = db.query(User.name).filter(User.id == employee.id).first()
    if not user_name:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": employee.id,
        "name": user_name[0],  # Assuming user_name is a tuple (name,)
        "manager_id": employee.manager_id if employee.manager_id is not None else None,
        "job_title": employee.job_title if employee.job_title is not None else None,
        "organization_id": employee.organization_id if employee.organization_id is not None else None,
        "created_at": employee.created_at,
        "updated_at": employee.updated_at
    }

@router.put("/employee/profile/", response_model=EmployeeResponseForUpdate)
def update_employee_profile(current_user: UserDependency, updated_data: EmployeeCreate, db: Session = Depends(get_db)):
    user_id = current_user['id']
    employee = db.query(User).filter(User.id == user_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Update fields
    if updated_data.manager_id is not None:
        employee.manager_id = updated_data.manager_id
    if updated_data.job_title is not None:
        employee.job_title = updated_data.job_title
    if updated_data.organization_id is not None:
        employee.organization_id = updated_data.organization_id
    db.commit()
    db.refresh(employee)
    return employee


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