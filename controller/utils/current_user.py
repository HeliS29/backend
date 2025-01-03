from fastapi import HTTPException, status,Depends
from controller.auth import verify_jwt_token
from sqlalchemy.orm import Session
from typing import Dict, Any,Optional
from database import get_db
import os
from models.users import User
from jose import JWTError, jwt
from config import settings
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login") 

# def get_hashing_secret():
#     JWT_SECRET = os.getenv("JWT_SECRET", "default_secret")
#     JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
#     return JWT_SECRET, JWT_ALGORITHM, "other_optional_secret_value"



# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid authentication credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     payload = verify_jwt_token(token)
#     if payload is None:
#         raise credentials_exception
    
#     user_id: Optional[int] = payload.get("user_id")
#     if user_id is None:
#         raise credentials_exception

#     user = db.query(User).filter(User.id == user_id).first()
#     if user is None:
#         raise credentials_exception
#     return user
# async def get_current_user(token=Depends(oauth2_scheme)):
#     """Get current user"""
#     try:
#         # settings.JWT_SECRET, JWT_ALGORITHM, _ = get_hashing_secret()
#         # print(settings.JWT_SECRET)
#         payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
#         print(payload)

#         # Extract user_id and manager_id from the payload
#         user_id: str = payload.get("user_id")
#         manager_id: str = payload.get("manager_id")  # Get manager_id from the token
#         user_role: str = payload.get("role")

#         # Check if both user_id and manager_id are None
#         if not user_id and not manager_id:
#             raise HTTPException(
#                 status_code=401,
#                 detail="[get_current_user] Could not validate credentials"
#             )

#         # Return different response based on role and id
#         if user_role == "manager":
#             return { "id": None, "manager_id": manager_id, "user_role": user_role }
#         else:
#             return { "id": user_id, "manager_id": None, "user_role": user_role }

#     except JWTError:
#         raise HTTPException(status_code=401, detail="Could not validate credentials.")

async def get_current_user(token=Depends(oauth2_scheme)):
    """Get current user"""
    try:
        # print(settings.JWT_SECRET)
        # print(token)
        # print(settings.JWT_ALGORITHM)
        # print
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        # print(payload)
        user_id: str = payload.get("user_id")
        manager_id: str = payload.get("manager_id")
        # user_name: str = payload.get("")
        user_role: str = payload.get("role")
        if user_id is None and manager_id is None:
            raise HTTPException(
                status_code=401,
                detail=f"[get_current_user] Could not validate credentials{user_id}",
            )
        return { "id": user_id, "user_role": user_role,"manager_id":manager_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials.")