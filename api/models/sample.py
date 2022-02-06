from sqlalchemy import Column, Integer, String, ForeignKey

from api.db import Base


class Sample(Base):
  __tablename__ = 'sample'

  id = Column(Integer, primary_key=True)
  message = Column(String(1024))