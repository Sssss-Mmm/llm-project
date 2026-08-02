from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])

"""헬스 체크 API 엔드포인트를 정의한다."""
@router.get("/")
def root():
    return {
        "message": "LLM Backend Project",
        "version": "0.1.0"
    }
"""헬스 상태를 확인한다."""
@router.get("/status")
def health():
    return {
        "status": "ok"
        }