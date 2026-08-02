from abc import ABC, abstractmethod

from llm_backend.models.document import Document


class TextChunker(ABC):

    @abstractmethod
    def split(
        self,
        documents: list[Document],
    ) -> list[Document]:
        pass