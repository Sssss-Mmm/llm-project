from pydantic import BaseModel, Field


class Document(BaseModel):
    """문서를 나타내는 모델이다."""
    id: str = Field(
        min_length=1,
        max_length=100,
        description="문서의 고유 식별자",
        examples=["doc_12345"],
    )

    title: str = Field(
        min_length=1,
        max_length=200,
        description="문서의 제목",
        examples=["FastAPI란?"],
    )

    content: str = Field(
        min_length=1,
        max_length=10000,
        description="문서의 내용",
        examples=["FastAPI는 Python 기반의 웹 프레임워크이다."],
    )