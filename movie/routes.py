from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette import status
from sqlalchemy.orm import Session
from database import get_db
from typing import List

from .schemas import CreateMovie, GetMovies
from .services import get_movies_list, add_new_movie, search_by_name
from rating.services import average_ratings
from auth.security import get_current_user

router = APIRouter(
    tags=["Movie"],
    prefix="/movie",
    dependencies=[Depends(get_current_user)]
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GetMovies])
async def all_movies (db: Session = Depends(get_db)):
    return await get_movies_list(db)


@router.get("/search", status_code=status.HTTP_200_OK)
async def single_movie (name: str, db: Session = Depends(get_db)):
    res = await search_by_name(db, name)
    res["average_rating"] = average_ratings(res["id"], db)
    return res


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_movie (movie: CreateMovie, db: Session = Depends(get_db)):
    await add_new_movie(db, movie)

    payload = {
        "message" : "Movie added successfully",
        "data" : await get_movies_list(db)
    }

    return JSONResponse(content=payload)
