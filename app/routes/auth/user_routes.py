from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routes.auth.schemas.auth_schema import UserCreate, UserResponse
from crud.auth import create_user
from models.users import User,UserRole
from models.profile import Manager
# from models.profile import Employee

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the email is already registered
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create the new user
    new_user = create_user(db, user.name, user.email, user.password)

    # Ensure 'employee' role exists
    employee_role = db.query(UserRole).filter(UserRole.role == 'employee').first()
    if not employee_role:
        # Create 'employee' role if it doesn't exist
        employee_role = UserRole(role="employee")
        db.add(employee_role)
        db.commit()
        db.refresh(employee_role)

    # Ensure 'manager' role exists
    manager_role = db.query(UserRole).filter(UserRole.role == 'manager').first()
    if not manager_role:
        # Create 'manager' role if it doesn't exist
        manager_role = UserRole(role="manager")
        
        db.add(manager_role)
        db.commit()
        db.refresh(manager_role)

    # Assign the appropriate role ID to the user
    new_user.role_id = employee_role.id
    if user.role.lower() == 'manager':
        new_user.role_id = manager_role.id
    db.commit()
    db.refresh(new_user)

    # If the user has a 'manager' role, ensure the Manager table has the details
    if user.role.lower() == 'manager':
        manager_entry = db.query(Manager).filter(Manager.email == user.email).first()
        if not manager_entry:
            # Add the manager details
            new_manager = Manager(
                name=user.name,
                email=user.email,
                # dept=user.dept if user.dept else None,
                 # Assuming `dept` is part of UserCreate schema
            )
            db.add(new_manager)
            db.commit()
            db.refresh(new_manager)

    return new_user

