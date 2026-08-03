from abc import ABC, abstractmethod

from llm_backend.models.embedded_document import EmbeddedDocument
from llm_backend.models.search_result import SearchResult

class VectorStore(ABC):
    """벡터 스토어의 추상 클래스이다."""

    @abstractmethod
    def save(
        self,
        documents: list[EmbeddedDocument],
    ) -> None:
        """임베딩된 문서를 벡터 스토어에 저장한다."""
        pass

    @abstractmethod
    def search(
        self,
        query_embedding: list[float],
        top_k: int = 5,
    ) -> list[SearchResult]:
        """쿼리 임베딩과 가장 유사한 문서를 벡터 스토어에서 검색한다."""
        pass

    @abstractmethod
    def delete(
        self,
        document_id: str,
    ) -> None:
        """벡터 스토어에서 문서를 삭제한다."""
        pass