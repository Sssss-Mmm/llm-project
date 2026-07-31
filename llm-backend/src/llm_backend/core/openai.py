from openai import OpenAI

from llm_backend.core.config import settings

client = OpenAI(
    api_key=settings.openai_api_key
    )
