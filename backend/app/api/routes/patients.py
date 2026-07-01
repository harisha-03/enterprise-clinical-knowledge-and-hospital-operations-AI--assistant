from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.patient_schema import (
    PatientCreate,
    PatientResponse
)

from app.services.patient_service import (
    get_all_patients,
    get_patient_by_id,
    search_patients,
    create_patient
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.get("/", response_model=List[PatientResponse])
def read_patients(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_patients(db, skip, limit)


@router.get("/search", response_model=List[PatientResponse])
def search_patient(
    name: str,
    db: Session = Depends(get_db)
):
    return search_patients(db, name)


@router.get("/{patient_id}", response_model=PatientResponse)
def read_patient(
    patient_id: str,
    db: Session = Depends(get_db)
):
    patient = get_patient_by_id(db, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@router.post("/", response_model=PatientResponse)
def add_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return create_patient(db, patient)