from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.laboratory_schema import LaboratoryResponse

from app.services.laboratory_service import (
    get_all_lab_results,
    get_patient_lab_results
)

router = APIRouter(
    prefix="/lab-results",
    tags=["Laboratory Results"]
)


@router.get("/", response_model=List[LaboratoryResponse])
def read_lab_results(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_lab_results(db, skip, limit)


@router.get("/{patient_id}", response_model=List[LaboratoryResponse])
def read_patient_lab_results(
    patient_id: str,
    db: Session = Depends(get_db)
):
    return get_patient_lab_results(db, patient_id)