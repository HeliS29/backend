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