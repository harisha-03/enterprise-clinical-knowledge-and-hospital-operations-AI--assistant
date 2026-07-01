from sqlalchemy import Column, String, Date, Time, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Admission(Base):
    __tablename__ = "admissions"

    admission_id = Column(String, primary_key=True)
    patient_id = Column(String)
    doctor_id = Column(String)
    bed_id = Column(String)
    admission_date = Column(Date)
    admission_time = Column(Time)
    admission_reason = Column(String)
    admission_type = Column(String)
    expected_discharge_date = Column(Date)
    status = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())