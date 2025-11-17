from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Habit Tracker API",
    description="API for tracking daily habits",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Habit Tracker API is running"}


@app.post("/habits", response_model=schemas.Habit)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    """Create a new habit."""
    return crud.create_habit(db=db, habit=habit)


@app.get("/habits", response_model=List[schemas.Habit])
def list_habits(db: Session = Depends(get_db)):
    """Get all habits."""
    return crud.get_habits(db=db)


@app.patch("/habits/{habit_id}/toggle", response_model=schemas.Habit)
def toggle_habit(habit_id: int, db: Session = Depends(get_db)):
    """Toggle the completion status of a habit."""
    habit = crud.toggle_habit(db=db, habit_id=habit_id)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit
