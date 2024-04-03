from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Annotated
from jose import JWTError, jwt

from user.models import UserModel
from database import get_db


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password) -> str:
    return password_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return password_context.verify(plain_password, hashed_password)


def get_user(id: int, db):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    return user


def authenticate_user(email: str, password: str, db: Session):
    user = db.query(UserModel).filter(UserModel.email == email).first()

    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("id")

        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(id, db)

    if user is None:
        raise credentials_exception
    return user


