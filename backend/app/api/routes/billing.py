from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.billing_schema import BillingResponse

from app.services.billing_service import (
    get_all_bills,
    get_patient_bills
)

router = APIRouter(
    prefix="/billing",
    tags=["Billing"]
)


@router.get("/", response_model=List[BillingResponse])
def read_bills(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_bills(db, skip, limit)


@router.get("/{patient_id}", response_model=List[BillingResponse])
def read_patient_bills(
    patient_id: str,
    db: Session = Depends(get_db)
):
    return get_patient_bills(db, patient_id)