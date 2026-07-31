from pydantic import BaseModel, Field 

class ChatRequest(BaseModel):
    conversation_id: str = Field(
        min_length=1,
        max_length=100,
        description="대화 세션을 구분하기 위한 고유한 ID",
        example="session_12345"
    ),
    message: str = Field(
        min_length=1,
        max_length=2000,
        description="사용자가 입력한 메시지",
        example="안녕하세요, 오늘 날씨가 어떤가요?"
    )
    
class ChatResponse(BaseModel):
    reply: str