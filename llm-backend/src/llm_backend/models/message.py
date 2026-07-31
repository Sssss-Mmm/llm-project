from pydantic import BaseModel, Field

from llm_backend.models.role import Role

class Message(BaseModel):
    role : Role
    content : str