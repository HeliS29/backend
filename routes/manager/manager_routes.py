from fastapi import APIRouter, Depends, HTTPException
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
def get_users_by_manager(current_user:UserDependency,db: Session = Depends(get_db)):
    # Check if the manager exists
    manager_id=None
    if current_user["manager_id"]:
        manager_id=current_user["manager_id"]
    manager = db.query(Manager).filter(Manager.id == manager_id).first()
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    # Fetch users assigned to the manager
    users = db.query(User).filter(User.manager_id == manager_id).all()

    if not users:
        raise HTTPException(status_code=404, detail="No users assigned to this manager")

    return users