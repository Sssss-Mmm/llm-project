from abc import ABC, abstractmethod

from llm_backend.models.document import Document
from llm_backend.models.embedded_document import EmbeddedDocument


class EmbeddingProvider(ABC):
    
    """임베딩을 생성하는 Provider의 추상 클래스이다."""
    @abstractmethod
    def embed(
        self,
        documents: list[Document],
    ) -> list[EmbeddedDocument]:
        pass