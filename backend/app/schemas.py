from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None


class HabitCreate(HabitBase):
    pass


class HabitResponse(HabitBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    completed: bool
    created_at: datetime
