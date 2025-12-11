from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.tasksRepository import TasksRepository

class TasksService:
    def getTasks(db: Session, user):
        return TasksRepository.getTasksByUser(db, user.ci)

    def setTask(db: Session, request):
        if not request.title:
            raise HTTPException(status_code=400, detail="Title required")

        if not request.description:
            raise HTTPException(status_code=400, detail="Description required")

        if not request.userci:
            raise HTTPException(status_code=400, detail="CI required")

        return TasksRepository.setTask(db, request)

    def updateTask(db: Session, taskId, request):
        task = TasksRepository.getTask(db, taskId)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        if request.title is not None and not request.title:
            raise HTTPException(status_code=400, detail="Title cannot be empty")

        if request.description is not None and not request.description:
            raise HTTPException(status_code=400, detail="Description cannot be empty")

        if request.userci is not None and not request.userci:
            raise HTTPException(status_code=400, detail="CI invalid")

        updated = TasksRepository.updateTask(db, taskId, request)
        if not updated:
            raise HTTPException(status_code=404, detail="Task not found")

        return updated


    def deleteTask(db: Session, taskId: int):
        task = TasksRepository.getTask(db, taskId)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        if TasksRepository.deleteTask(db, taskId):
            raise HTTPException(status_code=404, detail="Task not found")

        return {"message": "Task deleted"}