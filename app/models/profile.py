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
    dept = Column(String(100), nullable=True)
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())



class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


# class Employee(Base):
#     __tablename__ = "employees"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     manager_id = Column(Integer, ForeignKey("managers.id"), nullable=True)
#     job_title = Column(String(100), nullable=True)
#     organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
#     created_at = Column(DateTime,default=func.now())
    # updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # # Relationships
    # manager = relationship("Manager", backref="employees")
    # organization = relationship("Organization", backref="employees")
    
