from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.chat import HospitalAIChat

router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)

chat = HospitalAIChat()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat_endpoint(request: ChatRequest):

    return chat.ask(request.question)