import requests
from fastapi import HTTPException, status
from auth.security import get_password_hash
from .models import UserModel


# Create a new user
async def create_user(db, user):
    exists_user = db.query(UserModel).filter(UserModel.email == user.email).first()

    if exists_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    new_user = UserModel(
        name=user.name,
        phone=user.phone,
        password=get_password_hash(user.password),
        email=user.email
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

