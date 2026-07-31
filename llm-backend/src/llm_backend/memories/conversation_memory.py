from abc import ABC, abstractmethod
from llm_backend.models.message import Message


class ConversationMemory(ABC):

    @abstractmethod
    def load(self, conversation_id: str) -> list[Message]:
        pass

    @abstractmethod
    def save(self, conversation_id: str, message: Message) -> None:
        pass

    @abstractmethod
    def clear(self, conversation_id: str) -> None:
        pass