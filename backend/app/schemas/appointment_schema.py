from datetime import date, time
from pydantic import BaseModel


class AppointmentResponse(BaseModel):
    appointment_id: str
    patient_id: str
    doctor_id: str
    department_id: str
    appointment_date: date
    appointment_time: time
    appointment_type: str
    reason_for_visit: str
    status: str

    class Config:
        from_attributes = True