from llm_backend.embeddings.embedding_provider import EmbeddingProvider
from llm_backend.models.document import Document
from llm_backend.retrievers.retriever import Retriever
from llm_backend.vectorstores.vector_store import VectorStore


class VectorRetriever(Retriever):

    def __init__(
        self,
        embedding_provider: EmbeddingProvider,
        vector_store: VectorStore,
    ):
        """VectorRetriever를 초기화한다."""
        self.embedding_provider = embedding_provider
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Document]:
        """주어진 쿼리를 기반으로 문서를 검색한다."""
        query_embedding = self.embedding_provider.embed_query(
            query
        )

        results = self.vector_store.search(
            query_embedding,
            top_k,
        )

        return [
            result.document
            for result in results
        ]