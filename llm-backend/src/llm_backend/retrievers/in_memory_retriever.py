from llm_backend.models.document import Document
from llm_backend.retrievers.retriever import Retriever


class InMemoryRetriever(Retriever):
    """메모리에 저장된 문서를 검색하는 Retriever의 구현체이다."""
    def __init__(self):
        """InMemoryRetriever를 초기화한다."""
        self.documents = [
            Document(
                id="doc_1",
                title="FastAPI",
                content="FastAPI는 Python 기반의 웹 프레임워크이다.",
            ),
            Document(
                id="doc_2",
                title="Spring Boot",
                content="Spring Boot는 Java 기반의 웹 프레임워크이다.",
            ),
            Document(
                id="doc_3",
                title="RAG",
                content="RAG는 Retrieval Augmented Generation의 약자이다.",
            ),
        ]

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Document]:
        """주어진 쿼리를 기반으로 문서를 검색한다."""
        # 검색 로직은 단순히 문서의 제목과 내용에 쿼리가 포함되어 있는지 확인하는 방식으로 구현되어 있다.
        results = [
            doc for doc in self.documents
            if query.lower() in doc.title.lower() or query.lower() in doc.content.lower()
        ]
        return results[:top_k]

