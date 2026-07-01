from datetime import date

from sqlalchemy.orm import Session

from app.models.appointment import Appointment


def get_all_appointments(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(Appointment)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_appointment_by_id(
    db: Session,
    appointment_id: str
):
    return (
        db.query(Appointment)
        .filter(Appointment.appointment_id == appointment_id)
        .first()
    )


def get_todays_appointments(db: Session):
    return (
        db.query(Appointment)
        .filter(Appointment.appointment_date == date.today())
        .all()
    )