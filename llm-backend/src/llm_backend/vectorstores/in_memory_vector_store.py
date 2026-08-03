from llm_backend.models.embedded_document import EmbeddedDocument
from llm_backend.models.search_result import SearchResult
from llm_backend.utils.vector_math import VectorMath
from llm_backend.vectorstores.vector_store import VectorStore


class InMemoryVectorStore(VectorStore):

    def __init__(self):
        self.documents: dict[str, EmbeddedDocument] = {}

    def save(
        self,
        documents: list[EmbeddedDocument],
    ) -> None:
        """임베딩된 문서를 벡터 스토어에 저장한다."""
        for document in documents:
            self.documents[document.document.id] = document


    def delete(
        self,
        document_id: str,
    ) -> None:
        """벡터 스토어에서 문서를 삭제한다."""
        self.documents.pop(
            document_id,
            None,
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 5,
    ) -> list[SearchResult]:
        """쿼리 임베딩과 가장 유사한 문서를 벡터 스토어에서 검색한다."""
        results: list[SearchResult] = []

        for embedded_document in self.documents.values():
            # 쿼리 임베딩과 문서 임베딩의 코사인 유사도를 계산한다.
            score = VectorMath.cosine_similarity(
                query_embedding,
                embedded_document.embedding,
            )

            results.append(
                SearchResult(
                    document=embedded_document.document,
                    score=score,
                )
            )
        results.sort(key=lambda result: result.score, reverse=True)

        return results[:top_k]

    def update(
        self,
        document: EmbeddedDocument,
    ) -> None:
        """벡터 스토어에서 문서를 업데이트한다."""
        self.documents[document.document.id] = document
    