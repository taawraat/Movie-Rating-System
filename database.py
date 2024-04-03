from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

SQLALCHEMY_DATABASE_URL = 'postgresql://movies_db_owner:32UOmGolEATn@ep-raspy-hill-a1s0s2gk.ap-southeast-1.aws.neon.tech/movies_db?sslmode=require'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# initialize the database
def init_db():
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
