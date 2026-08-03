from llm_backend.embeddings.embedding_provider import EmbeddingProvider
from llm_backend.models.document import Document
from llm_backend.loaders.document_loader import DocumentLoader
from llm_backend.chunkers.text_chunker import TextChunker
from llm_backend.models.embedded_document import EmbeddedDocument
from llm_backend.vectorstores.vector_store import VectorStore


class DocumentService:
    """문서 관련 서비스를 제공하는 클래스이다."""

    def __init__(
            self,
            loader: DocumentLoader,
            chunker: TextChunker,
            embedding_provider: EmbeddingProvider,
            vector_store: VectorStore,
    ):
        """문서 서비스를 초기화한다."""
        self.loader = loader
        self.chunker = chunker
        self.embedding_provider = embedding_provider
        self.vector_store = vector_store

    def upload(
            self,
            file_path: str,
    ) -> None:
        """문서를 업로드하고 벡터 스토어에 저장한다."""
        documents = self.loader.load(file_path)
        chunked_documents = self.chunker.split(documents)
        embedded_documents = self.embedding_provider.embed(chunked_documents)
        self.vector_store.save(embedded_documents)