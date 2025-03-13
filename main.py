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

@app.get("/")
def get_task():
    return "Hello world"

@app.put("/")
def root():
    return "Hello world"

@app.put("/")
def update_task():
    return "Hello world"

@app.delete("/")
def root():
    return "Hello world"

@app.post("/")
def root():
    return "Hello world"
