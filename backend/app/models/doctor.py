from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(String, primary_key=True)
    department_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    specialization = Column(String)
    qualification = Column(String)
    experience_years = Column(Integer)
    phone = Column(String)
    email = Column(String)
    consultation_fee = Column(Numeric)
    status = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())