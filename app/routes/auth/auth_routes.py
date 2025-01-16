from fastapi import APIRouter, Depends, HTTPException
from controller.utils.current_user import get_current_user
from sqlalchemy.orm import Session
from database import get_db
from models.users import User,UserRole
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from controller.auth import create_jwt_token,send_verification_code
from routes.auth.schemas.auth_schema import TokenResponse , PasswordResetConfirm,PasswordResetRequest,UserLogin,UserResponsenew
from crud.auth import authenticate_user,create_verification_code,verify_code
# from controller.utils.reset_email import send_reset_email
from passlib.context import CryptContext
from models.profile import Manager
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()
OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]

UserDependency = Annotated[dict, Depends(get_current_user)]

def hash_password(password: str) -> str:
    return pwd_context.hash(password)



@router.post("/login", response_model=TokenResponse)
def login(user: OAuth2Form, db: Session = Depends(get_db)):
    email = user.username
    password = user.password
    
    # First, check if the provided credentials are correct (superadmin credentials)
    if email == "superadmin@gmail.com" and password == "admin123":
        # Check if 'superadmin' role exists in the database, create if it doesn't
        superadmin_role = db.query(UserRole).filter(UserRole.role == 'superadmin').first()
        if not superadmin_role:
            superadmin_role = UserRole(role="superadmin")
            db.add(superadmin_role)
            db.commit()
            db.refresh(superadmin_role)
        
        # Check if superadmin user exists in the database, create if it doesn't
        superadmin_user = db.query(User).filter(User.email == email).first()
        if not superadmin_user:
            new_user = User(
                name="Admin",
                email=email,
                password_hash=hash_password(password),  # In production, hash the password before saving it
                role_id=superadmin_role.id
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        
        # Set response data for superadmin login
        response_data = {
            "user_id": None,
            "role": "superadmin",
            "manager_id": None
        }
    else:
        # Authenticate user for non-superadmin login
        authenticated_user = authenticate_user(db, email, password)
        if not authenticated_user:
            raise HTTPException(status_code=400, detail="Invalid credentials")

        # Fetch role details based on role_id
        role_id = authenticated_user.role_id
        if not role_id:
            raise HTTPException(status_code=400, detail="User role not assigned")

        role = db.query(UserRole).filter(UserRole.id == role_id).first()
        if not role:
            raise HTTPException(status_code=400, detail="Invalid role ID")

        role_name = role.role.lower()

        # Prepare response data based on role
        if role_name == "manager":
            manager = db.query(Manager).filter(Manager.email == email).first()
            if not manager:
                raise HTTPException(status_code=404, detail="Manager not found")
            
            response_data = {
                "user_id": None,
                "role": role_name,
                "manager_id": manager.id if manager.id else None
            }
        else:
            response_data = {
                "user_id": authenticated_user.id,
                "role": role_name,
                "manager_id": None
            }

    # Create JWT token for response
    token = create_jwt_token(response_data)

    return {
        "access_token": token,
        "token_type": "Bearer",
        **response_data  # Return either user_id or manager_id based on role
    }




@router.post("/password-reset", response_model=dict)
def request_password_reset(request: PasswordResetRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Email not registered")

    # Generate and store the verification code
    verification_code = create_verification_code(db, user)

    # Send the code to the user's email
    send_verification_code(user.email, verification_code)
    return {"message": "Password reset code sent to your email"}

@router.post("/password-reset/confirm", response_model=dict)
def confirm_password_reset(data: PasswordResetConfirm, db: Session = Depends(get_db)):
    # Use the email and verification code to find the user
    user = verify_code(db, data.email, data.verification_code)
    print(user)  # Match email and verification code
    if not user:
        print(f"Invalid or expired verification code: {data.verification_code} for email: {data.email}")
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")

    # Update password (hash the new password)
    user.password_hash = pwd_context.hash(data.new_password)
    user.verification_code = None  # Clear the used code
    user.verification_code_expires_at = None
    db.commit()
    return {"message": "Password reset successful"}



blacklisted_tokens = set()

@router.post("/logout")
def logout(token: str, db: Session = Depends(get_db)):
    # Add the token to a blacklist or invalidate the session
    blacklisted_tokens.add(token)
    return {"msg": "Logged out successfully"}

