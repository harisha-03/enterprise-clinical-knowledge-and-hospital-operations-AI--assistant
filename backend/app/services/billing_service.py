from sqlalchemy.orm import Session

from app.models.billing import Billing


def get_all_bills(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(Billing)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_patient_bills(
    db: Session,
    patient_id: str
):
    return (
        db.query(Billing)
        .filter(Billing.patient_id == patient_id)
        .all()
    )