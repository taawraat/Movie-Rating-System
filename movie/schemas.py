from pydantic import BaseModel, constr, validator
from datetime import datetime
from fastapi import HTTPException

class MovieBase(BaseModel):
    name: str
    genre: str
    rating: str
    release_date: str

    class Config:
        from_attributes = True


class CreateMovie(MovieBase):
    @validator('release_date')
    def validate_release_date(cls, v):
        try:
            datetime.strptime(v, '%d-%m-%Y')
        except ValueError as e:
            raise HTTPException(status_code=400, detail="Invalid date format. Date format should be dd-mm-yyyy")
        return v

    class Config:
        from_attributes = True


class GetMovies(BaseModel):
    id: int
    name: str
    genre: str
    rating: str
    release_date: str

    @validator('release_date')
    def validate_release_date(cls, v):
        try:
            datetime.strptime(v, '%d-%m-%Y')
        except ValueError as e:
            raise HTTPException(status_code=400, detail="Invalid date format. Date format should be dd-mm-yyyy")
        return v

    class Config:
        from_attributes = True
