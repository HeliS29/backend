from fastapi import APIRouter, Depends, HTTPException
from models.users import UserRole
from controller.utils.current_user import get_current_user
from sqlalchemy.orm import Session
from typing import Annotated, List
from routes.manager.schema.manager_schema import UserResponse

# Assuming necessary imports for models and database connection
from models import User, Manager
from database import get_db

router = APIRouter()


UserDependency = Annotated[dict, Depends(get_current_user)]
@router.get("/managers/users/", response_model=List[UserResponse])
def get_users_by_manager(current_user: UserDependency, db: Session = Depends(get_db)):
    # Check if the manager exists
    manager_id = current_user.get("manager_id")
    if not manager_id:
        raise HTTPException(status_code=400, detail="Manager ID not found")

    manager = db.query(Manager).filter(Manager.id == manager_id).first()
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    # Fetch users assigned to the manager and include role information from UserRole
    users = (
        db.query(User, UserRole.role)
        .join(UserRole, User.role_id == UserRole.id)
        .filter(User.manager_id == manager_id)
        .all()
    )

    if not users:
        raise HTTPException(status_code=404, detail="No users assigned to this manager")

    # Return the list of users with their role included
    return [
        UserResponse(
            id=user[0].id,
            name=user[0].name,
            email=user[0].email,
            job_title=user[0].job_title,
            role=user[1]  # Add the role from UserRole
        )
        for user in users
    ]
# def get_users_by_manager(current_user:UserDependency,db: Session = Depends(get_db)):
#     # Check if the manager exists
#     manager_id=None
#     if current_user["manager_id"]:
#         manager_id=current_user["manager_id"]
#     manager = db.query(Manager).filter(Manager.id == manager_id).first()
#     if not manager:
#         raise HTTPException(status_code=404, detail="Manager not found")

#     # Fetch users assigned to the manager
#     users = db.query(User).filter(User.manager_id == manager_id).all()

#     if not users:
#         raise HTTPException(status_code=404, detail="No users assigned to this manager")

#     return users