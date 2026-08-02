from abc import ABC, abstractmethod

from llm_backend.models.document import Document


class Retriever(ABC):
    """문서를 검색하는 Retriever의 추상 클래스이다."""
    @abstractmethod
    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Document]:
        """주어진 쿼리를 기반으로 문서를 검색한다."""
        pass