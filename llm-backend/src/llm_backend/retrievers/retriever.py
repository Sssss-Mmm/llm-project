from abc import ABC, abstractmethod

from llm_backend.models.document import Document


class Retriever(ABC):

    @abstractmethod
    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Document]:
        pass