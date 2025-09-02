from sqlalchemy import Column , Integer  , String , DateTime
from sqlalchemy.sql import func  
from database import Base




class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    token = Column(String, unique=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
