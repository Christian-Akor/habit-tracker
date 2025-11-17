from sqlalchemy.orm import Session
from . import models, schemas


def get_habits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Habit).offset(skip).limit(limit).all()


def get_habit(db: Session, habit_id: int):
    return db.query(models.Habit).filter(models.Habit.id == habit_id).first()


def create_habit(db: Session, habit: schemas.HabitCreate):
    db_habit = models.Habit(name=habit.name, description=habit.description)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit


def toggle_habit(db: Session, habit_id: int):
    db_habit = get_habit(db, habit_id)
    if db_habit:
        db_habit.completed = not db_habit.completed
        db.commit()
        db.refresh(db_habit)
    return db_habit


def delete_habit(db: Session, habit_id: int):
    db_habit = get_habit(db, habit_id)
    if db_habit:
        db.delete(db_habit)
        db.commit()
    return db_habit
