import os

from databases import Database
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, create_engine
from sqlalchemy.sql import func


# DATABASE_URL = "postgresql://recognition:recognition@localhost:5432/reco"
DATABASE_URL = "postgresql://qpvnasuzcvdwee:d3aecc71083e8f279851285095d9a8cb33f470c5838badaedc5ff1e3ce2df9c5@localhost/detdicolajotpa"

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)