from llm_backend.core.openai import client
from llm_backend.core.config import settings
from llm_backend.core.exceptions import OpenAIException

class OpenAIProvider:
    def chat(self, message: str) -> str:
        try:
            response = client.responses.create(
                model=settings.openai_model,
                input=message
            )
            return response.output_text
        except Exception as e:
            raise OpenAIException("OpenAI 호출 실패") from e