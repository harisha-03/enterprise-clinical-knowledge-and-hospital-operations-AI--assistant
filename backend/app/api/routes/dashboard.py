from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.dashboard_schema import DashboardOverview

from app.services.dashboard_service import get_dashboard_overview

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/overview",
    response_model=DashboardOverview
)
def dashboard_overview(
    db: Session = Depends(get_db)
):
    return get_dashboard_overview(db)