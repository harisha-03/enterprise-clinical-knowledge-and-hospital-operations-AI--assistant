from pydantic import BaseModel


class DashboardOverview(BaseModel):
    total_patients: int
    total_doctors: int
    total_appointments: int
    total_admissions: int
    total_lab_results: int
    total_bills: int