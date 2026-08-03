import fitz

from llm_backend.loaders.document_loader import DocumentLoader
from llm_backend.models.document import Document


class PDFLoader(DocumentLoader):
    """PDF 파일을 로드하는 Loader 클래스이다."""
        

    def load(
        self,
        file_path: str,
    ) -> list[Document]:
        """PDF 파일을 로드하는 Loader 클래스이다."""

        pdf = fitz.open(file_path)

        documents = []

        for page_index, page in enumerate(pdf):

            documents.append(
                Document(
                    id=f"page_{page_index + 1}",
                    title=f"{page_index + 1}페이지",
                    content=page.get_text(),
                )
            )

        return documents