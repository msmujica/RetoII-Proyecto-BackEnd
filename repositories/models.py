from sqlalchemy import Column, Integer, String
from repositories.database import Base

class Users(Base):
    __tablename__ = "users"

    ci = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100))
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    jti = Column(String(36))