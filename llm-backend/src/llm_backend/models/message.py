from pydantic import BaseModel, Field

from llm_backend.models.role import Role

class Message(BaseModel):
    """메시지를 나타내는 모델이다."""
    role : Role
    content : str