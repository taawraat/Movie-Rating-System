from pydantic import BaseModel


class RatingSchema(BaseModel):
    movie_id: int
    user_id: int
    rating: float

    class Config:
        orm_mode = True