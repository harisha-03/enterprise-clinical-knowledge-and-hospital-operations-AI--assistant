from sqlalchemy import Column, String, Date, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class LaboratoryResult(Base):
    __tablename__ = "laboratory_results"

    lab_result_id = Column(String, primary_key=True)
    patient_id = Column(String)
    doctor_id = Column(String)
    department_id = Column(String)
    test_name = Column(String)
    test_category = Column(String)
    sample_type = Column(String)
    test_result = Column(String)
    result_status = Column(String)
    test_date = Column(Date)
    report_date = Column(Date)
    remarks = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())