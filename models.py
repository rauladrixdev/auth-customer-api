from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    _tablename_ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)