from sqlalchemy import Column, String, Numeric, Date, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Billing(Base):
    __tablename__ = "billing"

    bill_id = Column(String, primary_key=True)
    patient_id = Column(String)
    admission_id = Column(String)
    insurance_id = Column(String)
    bill_date = Column(Date)
    total_amount = Column(Numeric)
    insurance_coverage = Column(Numeric)
    amount_paid = Column(Numeric)
    payment_method = Column(String)
    payment_status = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())