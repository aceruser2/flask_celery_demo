from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

engine = create_engine(
    "postgresql://user:password@0.0.0.0:5432/postgresserver",
    query_cache_size=1200,
    echo=True,
    poolclass=NullPool,
    future=True,
)
# db_session = scoped_session(
#     sessionmaker(autocommit=False, autoflush=False, bind=engine)
# )
Base = declarative_base()
