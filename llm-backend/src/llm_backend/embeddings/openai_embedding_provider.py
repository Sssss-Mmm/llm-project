from llm_backend.core.config import settings
from llm_backend.core.exceptions import OpenAIException
from llm_backend.core.openai import client

from llm_backend.embeddings.embedding_provider import EmbeddingProvider

from llm_backend.models.document import Document
from llm_backend.models.embedded_document import EmbeddedDocument


class OpenAIEmbeddingProvider(EmbeddingProvider):

    def embed(
        self,
        documents: list[Document],
    ) -> list[EmbeddedDocument]:
        """문서 임베딩을 생성하는 Provider 클래스이다."""
        try:

            texts = [
                document.content
                for document in documents
            ]

            response = client.embeddings.create(
                model=settings.openai_embedding_model,
                input=texts,
            )

            embedded_documents = []

            for document, embedding in zip(
                documents,
                response.data,
            ):

                embedded_documents.append(
                    EmbeddedDocument(
                        document=document,
                        embedding=embedding.embedding,
                    )
                )

            return embedded_documents

        except Exception as e:
            raise OpenAIException(
                "Embedding 생성 실패"
            ) from e

    def embed_query(
        self,
        query: str,
    ) -> list[float]:
        """질문 임베딩을 생성하는 Provider 클래스이다."""
        try:

            response = client.embeddings.create(
                model=settings.openai_embedding_model,
                input=query,
            )

            return response.data[0].embedding

        except Exception as e:
            raise OpenAIException(
                "질문 Embedding 생성 실패"
            ) from e