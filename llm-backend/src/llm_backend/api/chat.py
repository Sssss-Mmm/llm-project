from fastapi import APIRouter, Depends

from llm_backend.core.dependencies import get_chat_service
from llm_backend.models.chat import ChatRequest, ChatResponse
from llm_backend.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):
    reply = chat_service.chat(
        request.conversation_id,
        request.message,
    )

    return ChatResponse(reply=reply)