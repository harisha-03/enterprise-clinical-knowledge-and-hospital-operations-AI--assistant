from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.patient import Patient


def get_all_patients(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(Patient)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_patient_by_id(
    db: Session,
    patient_id: str
):
    return (
        db.query(Patient)
        .filter(Patient.patient_id == patient_id)
        .first()
    )


def search_patients(
    db: Session,
    name: str
):
    return (
        db.query(Patient)
        .filter(
            or_(
                Patient.first_name.ilike(f"%{name}%"),
                Patient.last_name.ilike(f"%{name}%")
            )
        )
        .all()
    )


def create_patient(db: Session, patient):

    last_patient = (
        db.query(Patient)
        .order_by(Patient.patient_id.desc())
        .first()
    )

    if last_patient:
        last_number = int(last_patient.patient_id.replace("PAT", ""))
        new_patient_id = f"PAT{last_number + 1:05d}"
    else:
        new_patient_id = "PAT00001"

    new_patient = Patient(
        patient_id=new_patient_id,
        first_name=patient.first_name,
        last_name=patient.last_name,
        gender=patient.gender,
        date_of_birth=patient.date_of_birth,
        blood_group=patient.blood_group,
        phone=patient.phone,
        email=patient.email,
        address=patient.address,
        city=patient.city,
        state=patient.state,
        country=patient.country,
        emergency_contact_name=patient.emergency_contact_name,
        emergency_contact_phone=patient.emergency_contact_phone,
        insurance_id=patient.insurance_id
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient