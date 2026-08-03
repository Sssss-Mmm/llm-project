from pydantic import BaseModel
from llm_backend.models.document import Document

class SearchResult(BaseModel):
    """검색 결과를 나타내는 모델이다."""
    document: Document
    score: float