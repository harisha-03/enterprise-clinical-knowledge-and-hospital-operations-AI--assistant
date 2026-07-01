from datetime import date
from pydantic import BaseModel, EmailStr


class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    blood_group: str
    phone: str
    email: EmailStr
    address: str
    city: str
    state: str
    country: str
    emergency_contact_name: str
    emergency_contact_phone: str
    insurance_id: str


class PatientResponse(BaseModel):
    patient_id: str
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    blood_group: str
    phone: str
    email: str
    city: str
    state: str
    country: str

    class Config:
        from_attributes = True