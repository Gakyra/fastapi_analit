from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class AnalyticsQuery(Base):
    __tablename__ = "analytics_queries"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    asset = Column(String(20), nullable=False)
    mode = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
