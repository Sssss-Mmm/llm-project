from abc import ABC, abstractmethod
from llm_backend.models.document import Document

class Retriever(ABC):
    @abstractmethod
    def retrieve(
        self,
        query: str,
    ) -> list[Document]:
        pass