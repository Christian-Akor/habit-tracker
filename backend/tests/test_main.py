from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from app.main import app
from app.database import Base, get_db

# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override the get_db dependency for testing."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    """Setup and teardown test database for each test."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "Habit Tracker API" in data["message"]


def test_create_habit():
    """Test creating a new habit."""
    habit_data = {
        "name": "Exercise",
        "description": "Do 30 minutes of exercise"
    }
    response = client.post("/habits", json=habit_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == habit_data["name"]
    assert data["description"] == habit_data["description"]
    assert data["completed"] is False
    assert "id" in data


def test_list_habits():
    """Test listing all habits."""
    # Create some habits first
    client.post("/habits", json={"name": "Habit 1", "description": "First habit"})
    client.post("/habits", json={"name": "Habit 2", "description": "Second habit"})
    
    response = client.get("/habits")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Habit 1"
    assert data[1]["name"] == "Habit 2"


def test_toggle_habit():
    """Test toggling a habit's completion status."""
    # Create a habit first
    create_response = client.post("/habits", json={"name": "Test Habit"})
    habit_id = create_response.json()["id"]
    
    # Toggle it to completed
    response = client.patch(f"/habits/{habit_id}/toggle")
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True
    
    # Toggle it back to not completed
    response = client.patch(f"/habits/{habit_id}/toggle")
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is False


def test_toggle_nonexistent_habit():
    """Test toggling a habit that doesn't exist."""
    response = client.patch("/habits/9999/toggle")
    assert response.status_code == 404
    assert response.json()["detail"] == "Habit not found"
