from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Habit Tracker API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to Habit Tracker API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/habits/", response_model=schemas.HabitResponse)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    return crud.create_habit(db=db, habit=habit)


@app.get("/habits/", response_model=List[schemas.HabitResponse])
def list_habits(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    habits = crud.get_habits(db, skip=skip, limit=limit)
    return habits


@app.get("/habits/{habit_id}", response_model=schemas.HabitResponse)
def get_habit(habit_id: int, db: Session = Depends(get_db)):
    db_habit = crud.get_habit(db, habit_id=habit_id)
    if db_habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return db_habit


@app.put("/habits/{habit_id}/toggle", response_model=schemas.HabitResponse)
def toggle_habit(habit_id: int, db: Session = Depends(get_db)):
    db_habit = crud.toggle_habit(db, habit_id=habit_id)
    if db_habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return db_habit


@app.delete("/habits/{habit_id}")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    db_habit = crud.delete_habit(db, habit_id=habit_id)
    if db_habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": "Habit deleted successfully"}
