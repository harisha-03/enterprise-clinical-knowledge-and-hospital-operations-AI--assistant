from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.router import api_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Enterprise AI Clinical Knowledge & Hospital Operations Assistant",
    description="Advanced RAG + Hospital Operations Platform",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix="/api/v1"
)

app.include_router(chat_router)