from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from services.loginService import LoginService
from services.tasksServices import TasksService
from repositories.database import get_db

router = APIRouter()

class TaskRequest(BaseModel):
    title: str
    description: str
    userci: int

class TaskUpdateRequest(BaseModel):
    title: str = None
    description: str = None
    userci: int = None
    isDeleted: bool = None


@router.get("/tasks")
def getTasks(db: Session = Depends(get_db), user = Depends(LoginService.requireAuth),):
    return TasksService.getTasks(db, user)

@router.post("/tasks")
def setTask(request: TaskRequest, db: Session = Depends(get_db), user = Depends(LoginService.requireAuth)):
    return TasksService.setTask(db, request)

@router.patch("/tasks/{taskId}")
def updateTask(taskId: int, request: TaskUpdateRequest, db: Session = Depends(get_db), user = Depends(LoginService.requireAuth),):
    return TasksService.updateTask(db, taskId, request)

@router.delete("/tasks/{taskId}")
def deleteTask(taskId: int, db: Session = Depends(get_db), user = Depends(LoginService.requireAuth),):
    return TasksService.deleteTask(db, taskId)