from sqlalchemy.orm import Session

from app.models.laboratory import LaboratoryResult


def get_all_lab_results(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(LaboratoryResult)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_patient_lab_results(
    db: Session,
    patient_id: str
):
    return (
        db.query(LaboratoryResult)
        .filter(LaboratoryResult.patient_id == patient_id)
        .all()
    )