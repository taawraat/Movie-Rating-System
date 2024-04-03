from sqlalchemy import Column, Integer, ForeignKey, Float
from database import Base

class RatingModel(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    rating = Column(Float, nullable=False)
