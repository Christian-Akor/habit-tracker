from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from app.main import app
from app.database import Base, get_db

# Use in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_create_habit():
    response = client.post(
        "/habits/",
        json={"name": "Exercise", "description": "Daily workout"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Exercise"
    assert data["description"] == "Daily workout"
    assert data["completed"] is False
    assert "id" in data


def test_list_habits():
    # Create some habits
    client.post("/habits/", json={"name": "Read", "description": "Read 30 minutes"})
    client.post("/habits/", json={"name": "Meditate", "description": "Morning meditation"})
    
    # List habits
    response = client.get("/habits/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Read"
    assert data[1]["name"] == "Meditate"


def test_get_habit():
    # Create a habit
    create_response = client.post(
        "/habits/",
        json={"name": "Yoga", "description": "Morning yoga"}
    )
    habit_id = create_response.json()["id"]
    
    # Get the habit
    response = client.get(f"/habits/{habit_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Yoga"


def test_get_habit_not_found():
    response = client.get("/habits/9999")
    assert response.status_code == 404


def test_toggle_habit():
    # Create a habit
    create_response = client.post(
        "/habits/",
        json={"name": "Drink Water", "description": "8 glasses a day"}
    )
    habit_id = create_response.json()["id"]
    
    # Toggle the habit (mark as completed)
    response = client.put(f"/habits/{habit_id}/toggle")
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True
    
    # Toggle again (mark as incomplete)
    response = client.put(f"/habits/{habit_id}/toggle")
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is False


def test_delete_habit():
    # Create a habit
    create_response = client.post(
        "/habits/",
        json={"name": "Sleep Early", "description": "Before 10 PM"}
    )
    habit_id = create_response.json()["id"]
    
    # Delete the habit
    response = client.delete(f"/habits/{habit_id}")
    assert response.status_code == 200
    
    # Verify it's deleted
    response = client.get(f"/habits/{habit_id}")
    assert response.status_code == 404
