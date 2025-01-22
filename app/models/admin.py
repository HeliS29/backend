from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime,Boolean

from sqlalchemy.sql import func
from database import Base 

class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)  # Use hashed passwords
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
