from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,func,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from models.users import User




class New_notification(Base):
    __tablename__ = 'new_notifications'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  
    manager_id = Column(Integer, ForeignKey("managers.id"), nullable=True) 
    is_read=Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now()) 