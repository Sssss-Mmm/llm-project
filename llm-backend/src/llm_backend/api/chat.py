from fastapi import APIRouter, Depends

from llm_backend.core.dependencies import get_chat_service
from llm_backend.services.chat_service import ChatService
from llm_backend.models.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["Chat"])
chatService = ChatService()

@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service),
):
    return ChatResponse(
        reply=service.chat(request.message)
    )