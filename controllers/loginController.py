from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from services.loginService import LoginService
from repositories.database import get_db

router = APIRouter()

# Flujo: Controller -> Service -> Repository

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return LoginService.login(db, request.email, request.password)
