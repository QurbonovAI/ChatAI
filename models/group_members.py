from sqlalchemy import Column , String , Integer, DateTime , TIMESTAMP , ForeignKey
from sqlalchemy.sql import func
from database import Base


class Group_Members(Base):
    __tablename__ = "group_members"
    id = Column(Integer , autoincrement=True , primary_key=True)
    group_id = Column(Integer , ForeignKey('groups.id'))
    user_id = Column(Integer , ForeignKey('users.id'))
    joined_at = Column(DateTime , server_default=func.now())