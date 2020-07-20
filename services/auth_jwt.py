from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users import FastAPIUsers

from schemas.user_schema import UserDB, User, UserCreate, UserUpdate
from db import database
from models.users import users


user_db = SQLAlchemyUserDatabase(UserDB, database, users)
SECRET = "djfdjdd9s93jd00fh38d83r32dbcs8s9a02b3jd0s"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)


fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)