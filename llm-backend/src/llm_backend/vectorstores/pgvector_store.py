from abc import ABC, abstractmethod

from llm_backend.models.document import Document
from llm_backend.models.message import Message


class PromptBuilder(ABC):
    """프롬프트를 생성하는 Builder의 추상 클래스이다."""
    @abstractmethod
    def build(
        self,
        messages: list[Message],
        documents: list[Document],
    ) -> list[dict]:
        """"프롬프트를 생성한다."""
        pass