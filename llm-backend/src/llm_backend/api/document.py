from fastapi import APIRouter, Depends, UploadFile, File
import tempfile
import shutil

from llm_backend.core.dependencies import get_document_service
from llm_backend.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post("/")
def upload_document(
    file: UploadFile = File(...),
    service: DocumentService = Depends(get_document_service),
):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf",
    ) as temp:

        shutil.copyfileobj(
            file.file,
            temp,
        )

        temp_path = temp.name

    service.upload(temp_path)

    return {
        "message": "업로드 완료"
    }