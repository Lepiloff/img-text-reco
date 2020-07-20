from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, Integer, String, DateTime

from db import Base


# Custom user
class UserTable(Base, SQLAlchemyBaseUserTable):

    name = Column(String(50))


users = UserTable.__table__




