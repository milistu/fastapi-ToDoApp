from fastapi import FastAPI
from models import ToDo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


todos = []


# Get all ToDos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}


# Get single ToDo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No ToDos found"}


# Create a ToDo
@app.post("/todos")
async def create_todos(todo: ToDo):
    todos.append(todo)
    return {"message": "ToDo has been added"}


# Update a ToDo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: ToDo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "No ToDos found to update"}


# Delete a ToDo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "ToDo has been DELETED"}
    return {"message": "No ToDos found"}
