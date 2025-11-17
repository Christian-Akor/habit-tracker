from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HabitBase(BaseModel):
    """Base schema for Habit."""
    name: str
    description: Optional[str] = None


class HabitCreate(HabitBase):
    """Schema for creating a new habit."""
    pass


class Habit(HabitBase):
    """Schema for Habit with all fields."""
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
