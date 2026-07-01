from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.appointment_schema import AppointmentResponse
from app.services.appointment_service import (
    get_all_appointments,
    get_appointment_by_id,
    get_todays_appointments
)

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.get("/", response_model=List[AppointmentResponse])
def read_appointments(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_appointments(db, skip, limit)


@router.get("/today", response_model=List[AppointmentResponse])
def todays_appointments(
    db: Session = Depends(get_db)
):
    return get_todays_appointments(db)


@router.get("/{appointment_id}", response_model=AppointmentResponse)
def read_appointment(
    appointment_id: str,
    db: Session = Depends(get_db)
):
    appointment = get_appointment_by_id(db, appointment_id)

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment