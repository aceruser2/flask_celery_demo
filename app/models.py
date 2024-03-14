from sqlalchemy import Column, Integer, String, Text, text, insert, event
from sqlalchemy.dialects.postgresql import UUID
from app.ext.db import db_session, engine, Base
from sqlalchemy.sql import func 


class Account(Base):
    __tablename__ = "account"

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    user = Column(Text, nullable=False)
    pw = Column(Text, nullable=False)


@event.listens_for(Account.__table__, "after_create")
def create_departments(tbl, conn, **kwargs):
    conn.execute(insert(tbl).values(user="organisation", pw="rrrr"))
