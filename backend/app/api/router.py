from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.patients import router as patients_router
from app.api.routes.doctors import router as doctors_router
from app.api.routes.appointments import router as appointments_router
from app.api.routes.admissions import router as admissions_router
from app.api.routes.laboratory import router as laboratory_router
from app.api.routes.billing import router as billing_router
from app.api.routes.dashboard import router as dashboard_router
api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(patients_router)
api_router.include_router(doctors_router)
api_router.include_router(appointments_router)
api_router.include_router(admissions_router)
api_router.include_router(laboratory_router)
api_router.include_router(billing_router)
api_router.include_router(dashboard_router)