from sqlalchemy import Column, String, Date, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    date_of_birth = Column(Date)
    blood_group = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String)
    insurance_id = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())