from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:ozodbek123@localhost:5432/ishonch"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False , autoflush=False , bind=engine)
Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

