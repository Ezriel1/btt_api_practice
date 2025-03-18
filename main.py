main.py
from task_model import Task #importing task from task model
from fastapi import FastAPI

app = FastAPI() #constructor 

tasks = [
    Task(),
    Task()
]

@app.get("/") #method to get
def root():
    return "Hello world"

@app.get("/get-tasks")
def get_all_tasks():
    return tasks

@app.get("/get-task")
def get_task(id):
    for task in tasks:
        if
    return 

@app.put("/put-task")
def root():
    return "Hello world"

@app.put("/")
def update_task():
    return "Hello world"

@app.delete("/delete")    
def delete_task(task_id = int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove()
    return "Hello world"

@app.post("/")
def root():
    return "Hello world"