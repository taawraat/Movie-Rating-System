from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated

from .security import authenticate_user, create_access_token
from database import get_db

router = APIRouter(
    tags=["Token"],
    prefix="/token",
)


@router.post("/")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"id": user.id, "email": user.email}
    )

    return {"message": "login successful!", "access_token": access_token, "token_type": "bearer"}
