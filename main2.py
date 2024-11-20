from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello2 World"}


# we'll make a simple todo list where we can add, delete, and update items.
todo = []


# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todo}


# Get a siingle todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo_one in todo:
        if todo_one.id == todo_id:

            return {"Sinlge todo_one": todo_one}
    else:
        return {"message": "Todo not found"}


# Add a todo
@app.post("/todos")
async def create_todo(todo_one: Todo):
    todo.append(todo_one)
    return {"message": "Todo has been created successfully."}


# Delete a todo
@app.delete("/todos/{todo_id}")
async def del_todo(todo_id: int):
    for todo_one in todo:
        if todo_one.id == todo_id:
            todo.remove(todo_one)
            return {"message": "Todo has been deleted successfully."}
    else:
        return {"message": "Todo not found"}


# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo_one in todo:
        if todo_one.id == todo_id:
            todo_one.item = todo_obj.item
            todo_one.id = todo_obj.id
            return {"New todo added": todo_obj}
    else:
        return {"message": "Todo not found"}