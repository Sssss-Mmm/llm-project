from llm_backend.core.config import settings
from llm_backend.core.exceptions import OpenAIException
from llm_backend.core.openai import client

from llm_backend.models.document import Document
from llm_backend.models.message import Message

from llm_backend.provider.llm_provider import LLMProvider
from llm_backend.prompts.prompt_builder import PromptBuilder


class OpenAIProvider(LLMProvider):

    def __init__(
        self,
        prompt_builder: PromptBuilder,
    ):
        self.prompt_builder = prompt_builder

    def chat(
        self,
        messages,
        documents,
    ):

        prompt = self.prompt_builder.build(
            messages,
            documents,
        )

        response = client.responses.create(
            model=settings.openai_model,
            input=prompt,
        )

        return response.output_text