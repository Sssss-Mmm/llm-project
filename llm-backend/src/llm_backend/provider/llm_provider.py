from abc import ABC, abstractmethod

from llm_backend.models.message import Message


class LLMProvider(ABC):

    @abstractmethod
    def chat(
        self,
        messages: list[Message],
    ) -> str:
        pass