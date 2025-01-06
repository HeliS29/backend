from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,func,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from models.users import User

# class Notification(Base):
#     __tablename__ = 'notifications'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
#     message = Column(String(100), nullable=False)
#     # is_read = Column(Boolean, default=False)  
#     is_read_by_user = Column(Boolean, default=False)  # Tracks if the user has read the notification
#     is_read_by_manager = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=func.now()) 
#     manager_id = Column(Integer, ForeignKey("managers.id"), nullable=True)
     



class New_notification(Base):
    __tablename__ = 'new_notifications'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  
    manager_id = Column(Integer, ForeignKey("managers.id"), nullable=True) 
    is_read=Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now()) 