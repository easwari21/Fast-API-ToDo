# Fast-API-ToDo

A REST API for managing To-Do items built with FastAPI and SQLAlchemy. This project demonstrates CRUD operations with a modern Python web framework.

## Features

- Create, read, update, and delete to-do items
- SQLAlchemy ORM for database operations
- Pydantic validation for request/response data
- Environment variable configuration
- Interactive API documentation with Swagger UI

## Tech Stack

- FastAPI - Web framework
- SQLAlchemy - SQL toolkit and ORM
- Pydantic - Data validation
- Python 3.7+

## Project Structure

```
Fast-API-ToDo/
├── main.py          # API routes and application
├── models.py        # Database models
├── schemas.py       # Pydantic schemas
├── database.py      # Database configuration
├── .env             # Environment variables
└── README.md        # This file
```

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/easwari21/Fast-API-ToDo.git
cd Fast-API-ToDo
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy python-dotenv
```

4. Create .env file:
```env
DATABASE_URL=sqlite:///./todos.db
```

5. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Create a To-Do
POST `/todos`
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
```

### Get All To-Dos
GET `/todos`

### Get a Specific To-Do
GET `/todos/{todo_id}`

### Update a To-Do
PUT `/todos/{todo_id}`
```json
{
  "title": "Buy groceries",
  "description": "Updated description",
  "completed": true
}
```

### Delete a To-Do
DELETE `/todos/{todo_id}`

## Interactive Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## File Descriptions

**main.py** - Contains all API route handlers and CRUD operations with error handling.

**models.py** - Defines the Todo SQLAlchemy model with fields: id, title, description, completed.

**schemas.py** - Pydantic models for validation:
- TodoBase: Common fields
- TodoCreate: For creating new to-dos
- Todo: Complete schema with ID

**database.py** - Database connection and session management using environment variables.

## Database Configuration

For SQLite (default):
```env
DATABASE_URL=sqlite:///./todos.db
```

For PostgreSQL:
```env
DATABASE_URL=postgresql://user:password@localhost/tododb
```

Install PostgreSQL driver: `pip install psycopg2-binary`
