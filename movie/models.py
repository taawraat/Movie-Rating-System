from sqlalchemy import Column, Integer, String, Date
from database import Base


# Movies table model
class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    rating = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
