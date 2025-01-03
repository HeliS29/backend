
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime

from sqlalchemy.sql import func
from database import Base  

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    report_version_id = Column(Integer, ForeignKey('report_versions.id'), nullable=False)
    comment_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())