from sqlalchemy.orm import Session
from . import models, schemas


def get_habits(db: Session):
    """Get all habits."""
    return db.query(models.Habit).all()


def create_habit(db: Session, habit: schemas.HabitCreate):
    """Create a new habit."""
    db_habit = models.Habit(name=habit.name, description=habit.description)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit


def toggle_habit(db: Session, habit_id: int):
    """Toggle the completion status of a habit."""
    db_habit = db.query(models.Habit).filter(models.Habit.id == habit_id).first()
    if db_habit:
        db_habit.completed = not db_habit.completed
        db.commit()
        db.refresh(db_habit)
    return db_habit
