# Habit Tracker

A full-stack web application for tracking daily habits, built with FastAPI, React, TypeScript, and Docker.

## Features

- Create and manage daily habits
- Track habit completion status
- Toggle habit completion for each day
- Responsive UI design for mobile and desktop
- RESTful API backend
- Dockerized development environment

## Tech Stack

**Backend:**
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- Pytest (Testing)

**Frontend:**
- React with TypeScript
- Vite (Build tool)
- Vitest & React Testing Library (Testing)

**DevOps:**
- Docker & Docker Compose
- GitHub Actions CI/CD

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine
- (Optional) Python 3.9+ and Node.js 18+ for local development

### Running with Docker Compose (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/Christian-Akor/habit-tracker.git
cd habit-tracker
```

2. Start the application:
```bash
docker-compose up
```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Running Tests

**Backend Tests:**
```bash
cd backend
pip install -r requirements.txt
pytest
```

**Frontend Tests:**
```bash
cd frontend
npm install
npm test
```

### Local Development (without Docker)

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
habit-tracker/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI application
│   │   ├── database.py      # Database configuration
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── schemas.py       # Pydantic schemas
│   │   └── crud.py          # CRUD operations
│   ├── tests/
│   │   └── test_main.py     # Backend tests
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── pytest.ini
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── __tests__/
│   │   │   └── App.test.tsx
│   │   ├── App.tsx          # Main React component
│   │   ├── App.css          # Styles
│   │   └── main.tsx         # Entry point
│   ├── Dockerfile
│   ├── package.json
│   ├── index.html
│   ├── vite.config.ts
│   └── tsconfig.json
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline
├── docker-compose.yml
├── .gitignore
└── README.md
```

## API Endpoints

- `GET /` - Health check
- `POST /habits` - Create a new habit
- `GET /habits` - List all habits
- `PATCH /habits/{habit_id}/toggle` - Toggle habit completion status

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is open source and available under the MIT License.