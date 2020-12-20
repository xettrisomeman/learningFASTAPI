from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title = "Simple Todo API", version = "4.2.0")

class Todo(BaseModel):
    username: str
    due_date: str
    description: str


# Create, Read, Update, Delete

store_todo = []


@app.get('/')
async def home():
    return {"hello" : "world"}



@app.post('/create_todo/')
async def create_todo(todo: Todo):
    store_todo.append(todo) # not good practices
    return todo.dict()



@app.get('/get_todos/', response_model = List[Todo])
async def get_all_todos():
    return store_todo



@app.get('/get_todo/{id}')
async def get_todo(id: int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo not found!")



@app.put('/put_todo/{id}')
async def update_todo(id: int, todo: Todo):
    try:
        store_todo[id] = todo
        return store_todo
    except:
        raise HTTPException(status_code=404, detail="Todo not found!")



@app.delete('/delete/{id}')
async def delete_todo(id: int):

    try:

        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo not found!")


