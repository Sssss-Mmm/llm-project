from pydantic import BaseModel

from llm_backend.models.document import Document


class EmbeddedDocument(BaseModel):
    """임베딩된 문서를 나타내는 모델이다."""
    document: Document

    embedding: list[float]

    """임베딩 벡터의 차원을 반환한다."""
    def dimension(self) -> int:
        return len(self.embedding)