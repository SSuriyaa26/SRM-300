from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLAlchemy_DATABASE_URL='postgresql://postgres:qwertyuiop@localhost/fastapi'
engine=create_engine(SQLAlchemy_DATABASE_URL)

SessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()








