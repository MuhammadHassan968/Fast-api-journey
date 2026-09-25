from fastapi import FastAPI, HTTPException, status

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Practice REST", "completed": False},
]


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for item in tasks:
        if item["id"] == task_id:
            return item
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_data: dict):
    new_id = len(tasks) + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": task_data.get("title", ""),
        "completed": task_data.get("completed", False),
    }
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: dict):
    for item in tasks:
        if item["id"] == task_id:
            item["title"] = task_data.get("title")
            item["completed"] = task_data.get("completed")
            return item
    raise HTTPException(status_code=404, detail="Task not found")


@app.patch("/tasks/{task_id}")
def patch_task(task_id: int, task_data: dict):
    for item in tasks:
        if item["id"] == task_id:
            if "title" in task_data:
                item["title"] = task_data["title"]
            if "completed" in task_data:
                item["completed"] = task_data["completed"]
            return item
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for index, item in enumerate(tasks):
        if item["id"] == task_id:
            tasks.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")