from openai import OpenAI

from llm_backend.core.config import settings

"""OpenAI Client를 생성한다."""
client = OpenAI(
    api_key=settings.openai_api_key
    )
