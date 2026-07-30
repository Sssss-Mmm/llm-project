from fastapi import APIRouter
from llm_backend.services.chat_service import ChatService
from llm_backend.models.chat import ChatRequest, ChatResponse
router = APIRouter(prefix="/chat", tags=["Chat"])
chatService = ChatService()
@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = chatService.chat(request.message)
    return ChatResponse(reply=response)