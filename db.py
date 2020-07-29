import os
from databases import Database
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

DEFAULT_DATABASE_URL = "postgresql://recognition:recognition@localhost:5432/reco"
DATABASE_URL = (os.getenv('DATABASE_URL', DEFAULT_DATABASE_URL))
BASEDIR = os.path.dirname(os.path.abspath(__file__))

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# databases query builder
database = Database(DATABASE_URL)

# Declare a base from your metadata
Base: DeclarativeMeta = declarative_base(metadata=metadata)