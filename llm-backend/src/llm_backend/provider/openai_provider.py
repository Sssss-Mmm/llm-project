from llm_backend.core.config import settings
from llm_backend.core.exceptions import OpenAIException
from llm_backend.core.openai import client
from llm_backend.models.message import Message
from llm_backend.provider.llm_provider import LLMProvider


class OpenAIProvider(LLMProvider):

    def chat(
        self,
        messages: list[Message],
    ) -> str:
        try:
            response = client.responses.create(
                model=settings.openai_model,
                input=self._to_openai_messages(messages),
            )

            return response.output_text

        except Exception as e:
            raise OpenAIException("OpenAI 호출 실패") from e

    def _to_openai_messages(
        self,
        messages: list[Message],
    ) -> list[dict]:
        return [
            {
                "role": message.role.value,
                "content": message.content,
            }
            for message in messages
        ]