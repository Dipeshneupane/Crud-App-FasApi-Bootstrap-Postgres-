from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Web(Base):
    __tablename__ = 'Web'

    id = Column(Integer, primary_key=True)
    name = Column(String)
