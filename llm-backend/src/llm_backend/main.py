from fastapi import FastAPI
from llm_backend.api.health import router as health_router
from llm_backend.api.chat import router as chat_router
from llm_backend.api.document import router as document_router

app = FastAPI()

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(document_router)