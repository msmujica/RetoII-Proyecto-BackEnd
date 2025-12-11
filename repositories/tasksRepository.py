from sqlalchemy.orm import Session
from repositories.models import Tasks


class TasksRepository:

    def getTasksByUser(db: Session, ci: int):
        return db.query(Tasks).filter(Tasks.userci == ci, Tasks.isdeleted == False).all()

    def getTask(db: Session, id: int):
        return db.query(Tasks).filter(Tasks.id == id).first()

    def setTask(db: Session, request):
        newTask = Tasks(
            title = request.title,
            description = request.description,
            userci = request.userci,
            isdeleted = False
        )
        db.add(newTask)
        db.commit()
        db.refresh(newTask)
        return newTask

    def updateTask(db: Session, taskId, request):
        obj = db.query(Tasks).filter(Tasks.id == taskId).first()
        if not obj:
            return None

        if request.title is not None:
            obj.title = request.title

        if request.description is not None:
            obj.description = request.description

        if request.userci is not None:
            obj.userci = request.userci

        if request.isDeleted is not None:
            obj.isdeleted = request.isDeleted

        db.commit()
        db.refresh(obj)
        return obj

    def deleteTask(db: Session, taskId):
        obj = db.query(Tasks).filter(Tasks.id == taskId).first()
        if not obj:
            return True

        obj.isdeleted = True
        db.commit()
        db.refresh(obj)
        return False