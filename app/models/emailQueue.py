from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,func,Boolean,Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class EmailQueue(Base):
    __tablename__ = 'email_queue'

    id = Column(Integer, primary_key=True, index=True)
    recipient_id = Column(Integer, nullable=False)
    recipient_type = Column(String(100), nullable=False)  # e.g., 'manager' or 'employee'
    subject = Column(String(100), nullable=False)
    body = Column(Text(), nullable=False)
    status = Column(String(100), default='pending')  # e.g., 'pending', 'sent', 'failed'
    created_at = Column(DateTime, default=func.now())
    sent_at = Column(DateTime, nullable=True)

