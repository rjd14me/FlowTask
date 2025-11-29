from .storage import load_tasks, save_tasks, generate_new_id
from .models import Task


def add_task(description):
    tasks = load_tasks()
    new_id = generate_new_id(tasks)
    task = Task(id=new_id, description=description)
    tasks.append(task.to_dict())
    save_tasks(tasks)


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            return


def delete_task(task_id):
    tasks = load_tasks()
    filtered = [task for task in tasks if task["id"] != task_id]
    filtered.sort(key=lambda t: t["id"])
    for idx, task in enumerate(filtered, start=1):
        task["id"] = idx
    save_tasks(filtered)
    return {"message": "Task deleted"}


def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "In progress"
            save_tasks(tasks)
            return


def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            return


def list_tasks(status=None):
    tasks = load_tasks()
    if status is None:
        return tasks
    return [task for task in tasks if task["status"] == status]
