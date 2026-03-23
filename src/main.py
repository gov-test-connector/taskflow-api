from fastapi import FastAPI, Query
from typing import Optional
from src.tasks import get_task, list_tasks
from src.projects import list_projects

app = FastAPI(title="taskflow-api", version="1.0.0")

@app.get("/tasks")
def get_tasks(status: Optional[str] = None, priority: Optional[str] = None):
    return list_tasks(status=status, priority=priority)

@app.get("/tasks/{task_id}")
def get_single_task(task_id: int):
    return get_task(task_id)

@app.get("/projects")
def get_projects():
    return list_projects()

@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}
