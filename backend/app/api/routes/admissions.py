from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.admission_schema import AdmissionResponse

from app.services.admission_service import (
    get_all_admissions,
    get_admission_by_id
)

router = APIRouter(
    prefix="/admissions",
    tags=["Admissions"]
)


@router.get("/", response_model=List[AdmissionResponse])
def read_admissions(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_admissions(db, skip, limit)


@router.get("/{admission_id}", response_model=AdmissionResponse)
def read_admission(
    admission_id: str,
    db: Session = Depends(get_db)
):
    admission = get_admission_by_id(db, admission_id)

    if admission is None:
        raise HTTPException(
            status_code=404,
            detail="Admission not found"
        )

    return admission