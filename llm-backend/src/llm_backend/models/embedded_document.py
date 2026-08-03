from pydantic import BaseModel
import math
from llm_backend.models.document import Document


class EmbeddedDocument(BaseModel):
    """임베딩된 문서를 나타내는 모델이다."""
    document: Document

    embedding: list[float]

