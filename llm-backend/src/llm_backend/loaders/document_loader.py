from abc import ABC, abstractmethod

from llm_backend.models.document import Document


class DocumentLoader(ABC):

    @abstractmethod
    def load(
        self,
        file_path: str,
    ) -> list[Document]:
        """파일을 읽어 Document 목록으로 변환한다."""
        pass