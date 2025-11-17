from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None


class HabitCreate(HabitBase):
    pass


class HabitResponse(HabitBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
