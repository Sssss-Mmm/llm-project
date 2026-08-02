from fastapi import Depends

from llm_backend.memories.conversation_memory import ConversationMemory
from llm_backend.memories.in_memory import InMemoryConversationMemory

from llm_backend.provider.llm_provider import LLMProvider
from llm_backend.provider.openai_provider import OpenAIProvider
from llm_backend.prompts.openai_prompt_builder import OpenAIPromptBuilder
from llm_backend.retrievers.retriever import Retriever
from llm_backend.retrievers.in_memory_retriever import InMemoryRetriever

from llm_backend.services.chat_service import ChatService

prompt_builder = OpenAIPromptBuilder()
provider = OpenAIProvider(
    prompt_builder
    )
memory = InMemoryConversationMemory()
retriever = InMemoryRetriever()

"""LLM Provider를 반환한다."""
def get_llm_provider() -> LLMProvider:
    return provider

"""Conversation Memory를 반환한다."""
def get_conversation_memory() -> ConversationMemory:
    return memory

"""Retriever를 반환한다."""
def get_retriever() -> Retriever:
    return retriever

"""Chat Service를 반환한다."""
def get_chat_service(
    provider: LLMProvider = Depends(get_llm_provider),
    memory: ConversationMemory = Depends(get_conversation_memory),
    retriever: Retriever = Depends(get_retriever),
) -> ChatService:

    return ChatService(
        provider=provider,
        memory=memory,
        retriever=retriever,
    )