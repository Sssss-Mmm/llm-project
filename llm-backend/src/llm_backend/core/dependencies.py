from fastapi import Depends

from llm_backend.memories.conversation_memory import ConversationMemory
from llm_backend.memories.in_memory import InMemoryConversationMemory
from llm_backend.provider.openai_provider import OpenAIProvider
from llm_backend.services.chat_service import ChatService

provider = OpenAIProvider()
memory = InMemoryConversationMemory()


def get_openai_provider() -> OpenAIProvider:
    return provider


def get_conversation_memory() -> ConversationMemory:
    return memory


def get_chat_service(
    provider: OpenAIProvider = Depends(get_openai_provider),
    memory: ConversationMemory = Depends(get_conversation_memory),
) -> ChatService:
    return ChatService(provider, memory)