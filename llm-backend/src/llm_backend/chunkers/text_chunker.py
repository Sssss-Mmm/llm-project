from abc import ABC, abstractmethod

from llm_backend.models.document import Document


class TextChunker(ABC):
    """문서를 분할하는 Chunker의 추상 클래스이다."""
    @abstractmethod
    def split(
        self,
        documents: list[Document],
    ) -> list[Document]:
        pass