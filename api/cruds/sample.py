from typing import List, Tuple, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.sample as sample_model
import api.schemas.sample as sample_schema


async def get_samples(db: AsyncSession) -> List[Tuple[int, str]]:
  result: Result = await (db.execute(
    select(
      sample_model.Sample.id,
      sample_model.Sample.message
    )
  ))
  return result.all()


async def get_sample(db: AsyncSession, sample_id: int) -> Optional[sample_model.Sample]:
  result: Result = await (db.execute(
      select(sample_model.Sample).filter(sample_model.Sample.id == sample_id)
  ))
  sample: Optional[Tuple[sample_model.Sample]] = result.first()
  return sample[0] if sample is not None else None


async def create_sample(
  db: AsyncSession, sample_create: sample_schema.SampleCreate
) -> sample_model.Sample:
  sample = sample_model.Sample(**sample_create.dict())
  db.add(sample)
  await db.commit()
  await db.refresh(sample)
  return sample


async def update_sample(
  db: AsyncSession, sample_create: sample_schema.SampleCreate, origin: sample_model.Sample
  ) -> sample_model.Sample:
  origin.message = sample_create.message
  db.add(origin)
  await db.commit()
  await db.refresh(origin)
  return origin


async def delete_sample(db: AsyncSession, origin: sample_model.Sample) -> None:
  await db.delete(origin)
  await db.commit()