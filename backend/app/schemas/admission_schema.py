from datetime import date, time
from pydantic import BaseModel


class AdmissionResponse(BaseModel):
    admission_id: str
    patient_id: str
    doctor_id: str
    bed_id: str
    admission_date: date
    admission_time: time
    admission_reason: str
    admission_type: str
    expected_discharge_date: date
    status: str

    class Config:
        from_attributes = True