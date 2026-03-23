from src.tasks import list_tasks, get_task

def test_list_all_tasks():
    result = list_tasks()
    assert isinstance(result, list)
    assert len(result) > 0

def test_filter_by_status():
    result = list_tasks(status="done")
    assert all(t["status"] == "done" for t in result)

def test_get_task_by_id():
    result = get_task(1)
    assert result["id"] == 1

def test_get_missing_task():
    result = get_task(999)
    assert "error" in result

def test_filter_by_priority():
    result = list_tasks(priority="high")
    assert all(t["priority"] == "high" for t in result)
