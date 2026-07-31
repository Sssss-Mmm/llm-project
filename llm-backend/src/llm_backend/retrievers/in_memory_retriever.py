from llm_backend.models.document import Document
from llm_backend.retrievers.retriever import Retriever


class InMemoryRetriever(Retriever):

    def __init__(self):
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
        # 간단한 검색 로직: query가 title 또는 content에 포함된 문서를 반환
        results = [
            doc for doc in self.documents
            if query.lower() in doc.title.lower() or query.lower() in doc.content.lower()
        ]
        return results[:top_k]

