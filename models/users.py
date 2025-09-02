from sqlalchemy import Column , String , Integer , TIMESTAMP
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer  , primary_key=True , autoincrement=True)
    username = Column(String , unique=True)
    password = Column(String)
    created_at = Column(TIMESTAMP , server_default=func.now())