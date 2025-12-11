from sqlalchemy.orm import Session
from repositories.models import Users

class LoginRepository:

    def getUserByEmail(db: Session, email: str):
        return db.query(Users).filter(Users.email == email).first()

    def updateUserToken(db: Session, email: str, jti: str):
        obj = db.query(Users).filter(Users.email == email).first()
        if not obj:
            return True

        obj.jti = jti
        db.commit()
        db.refresh(obj)
        return False
