from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import config
from db.models import Base

engine = create_engine(f'postgresql://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}')
Session = sessionmaker(bind=engine)
