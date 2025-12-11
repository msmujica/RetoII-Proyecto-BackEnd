from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from repositories.database import Base

class Users(Base):
    __tablename__ = "users"

    ci = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100))
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    jti = Column(String(36))

class Tasks(Base):
    __tablename__ = "tareas"


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    userci = Column(Integer, ForeignKey("users.ci"), nullable=False)
    isdeleted = Column(Boolean, nullable=False, default=False)