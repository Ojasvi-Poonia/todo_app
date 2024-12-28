from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict,List


app = FastAPI()

tasks: Dict[int, dict] = {}
counter = 1

class Task(BaseModel):
    title: str
    description: str  
    completed: bool = False

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None  
    completed: bool = None


@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    global counter
    task_data = task.dict()
    tasks[counter] = task_data
    tasks[counter]["id"] = counter
    counter+=1
    return tasks[counter-1]

#end point to retrieve all the tasks
@app.get("/tasks/",response_model=List[Task])
def get_all_tasks():
    return list(tasks.values())# Convert dictionary values to a list
@app.get("/tasks/{task_id}" , response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task
@app.put("/tasks/{task_id}",response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):

    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    task_data = task_update.dict(exclude_unset=True)
    for key,value in task_data.items(): # Loop through the fields to update
        task[key] = value
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404,detail="Task not found")
    del tasks[task_id]
    return {"details":"task deleted successfully"}


