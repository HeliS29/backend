
from sqlalchemy import Column, Integer, String, ForeignKey, Date,DateTime,func,Float,Sequence,Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class RoleReview(Base):
    __tablename__ = 'role_review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    purpose = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)
    organization = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    prepared_by = Column(String(100), nullable=False)
    # job_summary = Column(String(1000), nullable=False)
    job_summary = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class CoreFocusArea(Base):
    __tablename__ = 'core_focus_areas'

    id = Column(Integer, Sequence('core_focus_area_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    area = Column(String(100), nullable=False)
    time_spent = Column(Float, nullable=False)
    importance = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class CriticalActivities(Base):
    __tablename__ = 'critical_activities'

    id = Column(Integer, Sequence('core_focus_area_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    core_focus_area_id = Column(Integer, ForeignKey("core_focus_areas.id"), nullable=False)
    area = Column(String(100), nullable=False)
    importance = Column(Float, nullable=False)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class WorkData(Base):
    __tablename__ = 'workdata'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    work_description = Column(String(500), nullable=True)
    hours_description = Column(String(500), nullable=True)
    rows = Column(Text, nullable=False)  # Store rows as a JSON object
    comments = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
