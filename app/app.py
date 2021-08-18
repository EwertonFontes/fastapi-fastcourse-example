from fastapi import FastAPI
app = FastAPI()

todos = [
    {
        "id": "1",
        "Activity": "Study after work"
    },
    {
        "id": "2",
        "Activity": "Karate after study"
    }
]

@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"name": "ewerton"}

@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return({"data": todos})

@app.post('/todo', tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been added!"
    }

@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id: int, body:dict) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todo['Activity'] = body['Activity']
            return {
                "data": f"Todo with id {id} has been updated" 
            }
    return {
        "data": f"Todo with this id {id} number not found"
    }

@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return {
                "data": "To do has been deleted"
            }
    return {
        "data" "Todo not found"
    }
