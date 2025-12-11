from datetime import datetime, timedelta
import jwt
import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.loginRepository import LoginRepository

secretKey = "bbfd9ee2a536ed05d4b609ff305b09f54b5af49ac3e567456fa913d9137c9617"
algorithm = "HS256"
accessTokenMin = 60

class LoginService:

    def login(db: Session, email: str, password: str):
        user = LoginRepository.getUserByEmail(db, email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if user.password != password:
            raise HTTPException(status_code=404, detail="Incorrect password")

        token = LoginService.createToken(db, email)

        return {
            "token": token,
            "user": {
                "ci": user.ci,
                "email": user.email,
                "name": user.name,
                "lastName": user.lastname,
            }
        }

    def createToken(db: Session, email: str):
        now = datetime.utcnow()
        exp = now + timedelta(minutes=accessTokenMin)

        jti = str(uuid.uuid4())

        payload = {
            "sub": email,
            "exp": exp,
            "iat": now,
            "jti": jti
        }

        token = jwt.encode(payload, secretKey, algorithm=algorithm)

        updated = LoginRepository.updateUserToken(db, email, jti)

        if updated:
            raise HTTPException(status_code=401, detail="The token couldn't be updated with the user")

        return token

    def verifyToken(db: Session, token: str):
        try:
            decodedToken = jwt.decode(token, secretKey, algorithms=[algorithm])

            email = decodedToken.get("sub")
            jti = decodedToken.get("jti")

            if not email or not jti:
                raise HTTPException(status_code=401, detail="Invalid token")

            user = LoginRepository.getUserByEmail(db, email)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            db_jti = user.jti
            if not db_jti or db_jti != jti:
                raise HTTPException(status_code=401, detail="Invalid token or revoked token")

            return user

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Expired token")

        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
