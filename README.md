# Habit Tracker

A full-stack web application for tracking daily habits, built with FastAPI (Python) backend and React (TypeScript) frontend.

## Features

- ✅ Create and manage habits
- ✅ Mark habits as complete/incomplete
- ✅ Delete habits
- ✅ Responsive UI design for mobile and desktop
- ✅ RESTful API with FastAPI
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Automated tests for backend and frontend
- ✅ Docker support for easy deployment

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL ORM
- **SQLite** - Database
- **Pytest** - Testing framework

### Frontend
- **React** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Build tool
- **Vitest** - Testing framework

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for local development)

### Running with Docker (Recommended)

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
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Running Locally (Without Docker)

#### Backend

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the backend server:
```bash
uvicorn app.main:app --reload
```

4. Run backend tests:
```bash
pytest
```

#### Frontend

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Run frontend tests:
```bash
npm test
```

5. Build for production:
```bash
npm run build
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `POST /habits/` - Create a new habit
- `GET /habits/` - List all habits
- `GET /habits/{habit_id}` - Get a specific habit
- `PUT /habits/{habit_id}/toggle` - Toggle habit completion status
- `DELETE /habits/{habit_id}` - Delete a habit

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
│   │   └── crud.py          # Database operations
│   ├── tests/
│   │   └── test_main.py     # Backend tests
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── __tests__/
│   │   │   └── App.test.tsx # Frontend tests
│   │   ├── App.tsx          # Main App component
│   │   ├── App.css          # Styles
│   │   └── main.tsx         # Entry point
│   ├── Dockerfile
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## CI/CD

This project uses GitHub Actions for continuous integration. On every push and pull request to the main branch:
- Backend tests are run with pytest
- Frontend tests are run with vitest
- Frontend build is validated

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.