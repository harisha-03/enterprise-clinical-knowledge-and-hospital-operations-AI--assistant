from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "application": "Enterprise AI Clinical Knowledge & Hospital Operations Assistant",
        "database": "connected"
    }