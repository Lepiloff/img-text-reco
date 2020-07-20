from fastapi_users import models


class User(models.BaseUser):
    name: str


class UserCreate(models.BaseUserCreate):
    name: str


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
