import requests

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .schemas import CreateUserSchema, LoginSchema
from .services import create_user
from database import get_db


router = APIRouter(
    tags=["User"],
    prefix="/user",
)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: CreateUserSchema, db: Session = Depends(get_db)):
    await create_user(db, user)

    return {
        "message": "User created successfully",
        "data": user.dict()
    }


@router.post("/login", status_code=status.HTTP_200_OK)
def login(data: LoginSchema):
    user = {
        "username": data.email,
        "password": data.password
    }

    url = "http://localhost:8000/token"
    res = requests.post(url, data=user)

    return res.json()
