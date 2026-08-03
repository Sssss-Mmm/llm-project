from abc import ABC, abstractmethod

from llm_backend.models.document import Document
from llm_backend.models.embedded_document import EmbeddedDocument


class EmbeddingProvider(ABC):
    
    
    @abstractmethod
    def embed(
        self,
        documents: list[Document],
    ) -> list[EmbeddedDocument]:
        """임베딩을 생성하는 Provider의 추상 클래스이다."""
        pass

    @abstractmethod
    def embed_query(
        self,
        query: str,
    ) -> list[float]:
        """쿼리 임베딩을 생성하는 Provider의 추상 클래스이다."""
        pass