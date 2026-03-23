from src.config import SUPPORTED_STATUSES, SUPPORTED_PRIORITIES

# In-memory task store (placeholder — replace with DB in production)
_tasks = [
    {"id": 1, "title": "Set up CI pipeline", "status": "done", "priority": "high", "project_id": 1},
    {"id": 2, "title": "Write API documentation", "status": "in-progress", "priority": "medium", "project_id": 1},
    {"id": 3, "title": "Add authentication", "status": "open", "priority": "critical", "project_id": 1},
    {"id": 4, "title": "Write unit tests", "status": "open", "priority": "high", "project_id": 2},
    {"id": 5, "title": "Deploy to staging", "status": "open", "priority": "medium", "project_id": 2},
]

def list_tasks(status: str = None, priority: str = None) -> list:
    result = _tasks
    if status:
        result = [t for t in result if t["status"] == status]
    if priority:
        result = [t for t in result if t["priority"] == priority]
    return result

def get_task(task_id: int) -> dict:
    for task in _tasks:
        if task["id"] == task_id:
            return task
    return {"error": f"Task {task_id} not found"}
