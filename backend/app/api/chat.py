from fastapi import APIRouter
from pydantic import BaseModel

from app.retrieval.retrieval_service import RetrievalService

router = APIRouter()

rag = RetrievalService()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    response = rag.ask(request.question)

    return response