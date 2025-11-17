from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime, timezone
from .database import Base


class Habit(Base):
    """Habit model for tracking user habits."""
    
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
