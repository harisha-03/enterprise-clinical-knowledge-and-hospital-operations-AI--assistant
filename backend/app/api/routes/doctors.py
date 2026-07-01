from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.doctor_schema import DoctorResponse

from app.services.doctor_service import (
    get_all_doctors,
    get_doctor_by_id,
    search_doctors
)

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.get("/", response_model=List[DoctorResponse])
def read_doctors(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_doctors(db, skip, limit)


@router.get("/search", response_model=List[DoctorResponse])
def search_doctor(
    name: str,
    db: Session = Depends(get_db)
):
    return search_doctors(db, name)


@router.get("/{doctor_id}", response_model=DoctorResponse)
def read_doctor(
    doctor_id: str,
    db: Session = Depends(get_db)
):
    doctor = get_doctor_by_id(db, doctor_id)

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor