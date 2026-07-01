from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.doctor import Doctor


def get_all_doctors(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(Doctor)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_doctor_by_id(
    db: Session,
    doctor_id: str
):
    return (
        db.query(Doctor)
        .filter(Doctor.doctor_id == doctor_id)
        .first()
    )


def search_doctors(
    db: Session,
    name: str
):
    return (
        db.query(Doctor)
        .filter(
            or_(
                Doctor.first_name.ilike(f"%{name}%"),
                Doctor.last_name.ilike(f"%{name}%")
            )
        )
        .all()
    )