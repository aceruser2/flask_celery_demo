from sqlalchemy import Column, Integer, String, Text, text, insert, event
from sqlalchemy.dialects.postgresql import UUID
from app.ext.db import engine, Base
from sqlalchemy.sql import func


class Account(Base):
    __tablename__ = "account"

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    user = Column(Text, nullable=False)
    pw = Column(Text, nullable=False)


class Rate(Base):
    __tablename__ = "rate"
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    rate = Column(Integer, nullable=False)


@event.listens_for(Account.__table__, "after_create")
def create_departments(tbl, conn, **kwargs):
    conn.execute(insert(tbl).values(user="organisation", pw="rrrr"))
    conn.commit()
