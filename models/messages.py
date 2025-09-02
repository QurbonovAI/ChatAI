from sqlalchemy import Column , String , Integer , DateTime , ForeignKey
from sqlalchemy.sql import func
from database import Base


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer , )