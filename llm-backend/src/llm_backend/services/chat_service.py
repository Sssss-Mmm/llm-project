from llm_backend.provider.openai_provider import OpenAIProvider


class ChatService:
    def __init__(self):
        self.provider = OpenAIProvider()

    def chat(self, message: str) -> str:
        return self.provider.chat(message)