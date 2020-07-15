from databases import Database
from sqlalchemy import MetaData, create_engine


DATABASE_URL = "postgresql://recognition:recognition@localhost:5432/reco"
# DATABASE_URL = "postgresql://qpvnasuzcvdwee:d3aecc71083e8f279851285095d9a8cb33f470c5838badaedc5ff1e3ce2df9c5@localhost/detdicolajotpa"

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# databases query builder
database = Database(DATABASE_URL)