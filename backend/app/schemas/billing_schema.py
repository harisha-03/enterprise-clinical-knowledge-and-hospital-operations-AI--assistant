from datetime import date
from pydantic import BaseModel


class BillingResponse(BaseModel):
    bill_id: str
    patient_id: str
    admission_id: str
    insurance_id: str
    bill_date: date
    total_amount: float
    insurance_coverage: float
    amount_paid: float
    payment_method: str
    payment_status: str

    class Config:
        from_attributes = True