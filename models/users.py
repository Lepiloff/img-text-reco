from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Table, Column, Integer, String, DateTime
from db import Base, metadata

class UserTable(Base, SQLAlchemyBaseUserTable):
    # Add your columns here
    name = Column(String(50))

users = UserTable.__tablename__





