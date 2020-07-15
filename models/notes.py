from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db import metadata

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("test_field", String(50)),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

