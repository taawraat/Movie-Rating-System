from pydantic import BaseModel, EmailStr


class CreateUserSchema(BaseModel):
    name: str
    phone: str
    password: str
    email: EmailStr

    class Config:
        from_attributes = True


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
