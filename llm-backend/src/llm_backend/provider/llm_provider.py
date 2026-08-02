from abc import ABC, abstractmethod

from llm_backend.models.document import Document
from llm_backend.models.message import Message


class LLMProvider(ABC):
    """LLM을 제공하는 Provider의 추상 클래스이다."""
    @abstractmethod
    def chat(
        self,
        messages: list[Message],
        documents: list[Document],
    ) -> str:
        """LLM과 대화를 수행한다."""
        pass