from sqlalchemy import Column, String, Date, Time, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(String, primary_key=True)
    patient_id = Column(String)
    doctor_id = Column(String)
    department_id = Column(String)
    appointment_date = Column(Date)
    appointment_time = Column(Time)
    appointment_type = Column(String)
    reason_for_visit = Column(String)
    status = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())