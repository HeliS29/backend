from sqlalchemy import Column, Integer, ForeignKey, DateTime,String,Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Report(Base):
    __tablename__ = "reports"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # FK to Employee
    manager_id = Column(Integer, ForeignKey("managers.id"), nullable=False)
    current_version_id = Column(Integer, ForeignKey("report_versions.id"), nullable=True)
    pdf_path = Column(String(100), nullable=False)
    role=Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class ReportVersion(Base):
    __tablename__ = "report_versions"

    id = Column(Integer, primary_key=True, index=True)
    report_id = Column(Integer, ForeignKey("reports.id"), nullable=False)  
    version_number = Column(Integer, nullable=False)
    generated_at = Column(DateTime, default=func.now())
    pdf_path = Column(String(100), nullable=False)
    manager_comments = Column(Text, nullable=True)


class ReportContent(Base):
    __tablename__ = "report_contents"

    id = Column(Integer, primary_key=True, index=True)
    report_version_id = Column(Integer, ForeignKey("report_versions.id"), nullable=False)
    content = Column(Text, nullable=False)  # Storing text content

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<ReportContent(id={self.id}, report_version_id={self.report_version_id}, content={self.content})>"
