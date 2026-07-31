from abc import ABC, abstractmethod

from llm_backend.models.document import Document
from llm_backend.models.message import Message


class PromptBuilder(ABC):

    @abstractmethod
    def build(
        self,
        messages: list[Message],
        documents: list[Document],
    ) -> list[dict]:
        pass