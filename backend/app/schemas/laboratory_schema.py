from datetime import date
from pydantic import BaseModel


class LaboratoryResponse(BaseModel):
    lab_result_id: str
    patient_id: str
    doctor_id: str
    department_id: str
    test_name: str
    test_category: str
    sample_type: str
    test_result: str
    result_status: str
    test_date: date
    report_date: date
    remarks: str

    class Config:
        from_attributes = True