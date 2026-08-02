from llm_backend.chunkers.text_chunker import TextChunker
from llm_backend.models.document import Document


class RecursiveTextChunker(TextChunker):

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100,
    ):
        if overlap >= chunk_size:
            raise ValueError(
                "overlap은 chunk_size보다 작아야 합니다."
            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(
        self,
        documents: list[Document],
    ) -> list[Document]:

        chunks = []

        for document in documents:
            chunks.extend(
                self._split_document(document)
            )

        return chunks

    def _split_document(
        self,
        document: Document,
    ) -> list[Document]:

        chunks = []

        start = 0

        while start < len(document.content):

            end = start + self.chunk_size

            chunk_content = document.content[start:end]

            # 혹시 빈 문자열이면 종료
            if not chunk_content:
                break

            chunk_number = len(chunks) + 1

            chunks.append(
                Document(
                    id=f"{document.id}_chunk_{chunk_number}",
                    title=f"{document.title} - Chunk {chunk_number}",
                    content=chunk_content,
                )
            )

            start += self.chunk_size - self.overlap

        return chunks