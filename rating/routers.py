from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from auth.security import get_current_user
from .schemas import RatingSchema
from .services import create_rating
from database import get_db


router = APIRouter(
    tags=["Rating"],
    prefix="/rating",
    dependencies=[Depends(get_current_user)]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_rating(data: RatingSchema, db: Session = Depends(get_db)):
    await create_rating(db, data)

    return {
        "message": "Rating created successfully",
        "data": data.dict()
   }
