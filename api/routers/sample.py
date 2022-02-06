from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.sample as sample_schemas
import api.cruds.sample as sample_cruds
from api.db import get_db

router = APIRouter()


@router.get('/samples', response_model=List[sample_schemas.Sample])
async def get_samples(db: AsyncSession = Depends(get_db)):
  return await sample_cruds.get_samples(db)


@router.post('/sample', response_model=sample_schemas.SampleCreateResponse)
async def create_sample(
  sample_body: sample_schemas.SampleCreate, db: AsyncSession = Depends(get_db)):
  return await sample_cruds.create_sample(db, sample_body)


@router.put('/sample/{sample_id}', response_model=sample_schemas.SampleCreateResponse)
async def update_sample(sample_id: int, sample_body: sample_schemas.SampleCreate,
  db: AsyncSession = Depends(get_db)):

  sample = await sample_cruds.get_sample(db, sample_id=sample_id)
  if sample is None:
    raise HTTPException(status_code=404, detail='Sample not found')
  return await sample_cruds.update_sample(db, sample_body, origin=sample)


@router.delete('/sample/{sample_id}', response_model=None)
async def delete_sample(sample_id: int, db: AsyncSession = Depends(get_db)):
  sample = await sample_cruds.get_sample(db, sample_id=sample_id)
  if sample is None:
    raise HTTPException(status_code=404, detail="Sample not found")
  return await sample_cruds.delete_sample(db, origin=sample)