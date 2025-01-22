from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,func
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from models.users import User


class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    # dept = Column(String(100), nullable=True)
    organization_id = Column(Integer, ForeignKey("organizations.id",ondelete="CASCADE"), nullable=True)
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())




class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())



    
