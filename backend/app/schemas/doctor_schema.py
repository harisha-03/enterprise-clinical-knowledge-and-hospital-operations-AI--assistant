from pydantic import BaseModel, EmailStr


class DoctorResponse(BaseModel):
    doctor_id: str
    department_id: str
    first_name: str
    last_name: str
    specialization: str
    qualification: str
    experience_years: int
    phone: str
    email: EmailStr
    consultation_fee: float
    status: str

    class Config:
        from_attributes = True