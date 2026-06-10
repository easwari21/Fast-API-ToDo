from fastapi import FastAPI, Depends, HTTPException
from schemas import Todo as TodoSchema, TodoCreate
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import Todo

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fast-API-ToDo", version="1.0.0")


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos", response_model=TodoSchema, status_code=201)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new to-do item"""
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@app.get("/todos", response_model=list[TodoSchema])
def read_todos(db: Session = Depends(get_db)):
    """Get all to-do items"""
    return db.query(Todo).all()


@app.get("/todos/{todo_id}", response_model=TodoSchema)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a specific to-do item"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=TodoSchema)
def update_todo(
    todo_id: int, updated: TodoCreate, db: Session = Depends(get_db)
):
    """Update an existing to-do item"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    for key, value in updated.model_dump().items():
        setattr(todo, key, value)
    
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a to-do item"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    return {"detail": "Todo deleted successfully"}


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Welcome to Fast-API-ToDo", "docs": "/docs"}
