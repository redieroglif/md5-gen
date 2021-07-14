from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, Integer

Base = declarative_base()

class Task(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True)
    hash = Column(String)
    hash_ready = Column(Boolean)