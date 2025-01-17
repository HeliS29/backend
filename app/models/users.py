from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,func
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(16), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     password_hash = Column(String(100), nullable=False)
#     verification_code = Column(String(10), nullable=True) 
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now())
#     role_id = Column(Integer, ForeignKey("user_roles.id"), nullable=True)
#     organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
#     job_title = Column(String(50), nullable=True)
#     manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(16), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)
    verification_code = Column(String(10), nullable=True) 
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    role_id = Column(Integer, ForeignKey("user_roles.id"), nullable=True)
    purpose = Column(String(100), nullable=True)
    company_name = Column(String(100), nullable=True)
    job_title = Column(String(50), nullable=True)
    manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)



class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(50), nullable=False)
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime, default=func.now())
    






