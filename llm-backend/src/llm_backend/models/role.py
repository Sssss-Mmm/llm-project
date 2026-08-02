from enum import Enum

class Role(str, Enum):
    """메시지의 역할을 나타내는 Enum 클래스이다."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"