from typing import Optional

from pydantic import BaseModel, Field


class SampleBase(BaseModel):
  message: Optional[str] = Field(None, example='one picec.')


class SampleCreate(SampleBase):
  pass


class SampleCreateResponse(SampleCreate):
  id: int

  class Config:
    orm_mode = True


class Sample(SampleBase):
  id: int

  class Config:
    orm_mode = True
