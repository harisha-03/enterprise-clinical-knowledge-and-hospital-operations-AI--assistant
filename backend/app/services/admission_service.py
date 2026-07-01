from sqlalchemy.orm import Session

from app.models.admission import Admission


def get_all_admissions(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(Admission)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_admission_by_id(
    db: Session,
    admission_id: str
):
    return (
        db.query(Admission)
        .filter(Admission.admission_id == admission_id)
        .first()
    )