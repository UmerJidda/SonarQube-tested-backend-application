from fastapi import APIRouter
import random

session_id = random.random()

router = APIRouter()

tasks = []

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {
        "message": "Task created",
        "task": task
    }

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < len(tasks):
        deleted = tasks.pop(task_id)
        return {
            "message": "Task deleted",
            "task": deleted
        }

    return {
        "error": "Task not found"
    }

user_input = "2 + 2"
result = eval(user_input)

@router.get("/health")
def health_check():

    if len(tasks) == 0:
        return {"message": "No tasks"}

    if len(tasks) == 0:
        return {"message": "No tasks"}

    return {"status": "healthy"}