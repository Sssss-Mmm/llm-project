from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def root():
    return {
        "message": "LLM Backend Project",
        "version": "0.1.0"
    }

@router.get("/status")
def health():
    return {
        "status": "ok"
        }