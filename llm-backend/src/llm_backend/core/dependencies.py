from fastapi import Depends

from llm_backend.memories.conversation_memory import ConversationMemory
from llm_backend.memories.in_memory import InMemoryConversationMemory

from llm_backend.provider.llm_provider import LLMProvider
from llm_backend.provider.openai_provider import OpenAIProvider
from llm_backend.prompts.openai_prompt_builder import OpenAIPromptBuilder
from llm_backend.retrievers.retriever import Retriever
from llm_backend.retrievers.vector_retriever import VectorRetriever
from llm_backend.vectorstores.in_memory_vector_store import InMemoryVectorStore
from llm_backend.embeddings.openai_embedding_provider import OpenAIEmbeddingProvider
from llm_backend.loaders.pdf_loader import PDFLoader
from llm_backend.chunkers.recursive_text_chunker import RecursiveTextChunker 
from llm_backend.services.chat_service import ChatService
from llm_backend.services.document_service import DocumentService

# Prompt
prompt_builder = OpenAIPromptBuilder()
# provider
provider = OpenAIProvider(prompt_builder)
embedding_provider = OpenAIEmbeddingProvider()

# storage
vector_store = InMemoryVectorStore()
memory = InMemoryConversationMemory()

# Document
loader = PDFLoader()
chunker = RecursiveTextChunker()

# Retriever
retriever = VectorRetriever(
    embedding_provider,
    vector_store,
    )

# service
document_service = DocumentService(
    loader,
    chunker,
    embedding_provider,
    vector_store,
    )

"""LLM Provider를 반환한다."""
def get_llm_provider() -> LLMProvider:
    return provider

"""Conversation Memory를 반환한다."""
def get_conversation_memory() -> ConversationMemory:
    return memory

"""Retriever를 반환한다."""
def get_retriever() -> Retriever:
    return retriever

def get_chat_service(
    provider: LLMProvider = Depends(get_llm_provider),
    memory: ConversationMemory = Depends(get_conversation_memory),
    retriever: Retriever = Depends(get_retriever),
) -> ChatService:

    """Chat Service를 반환한다."""
    return ChatService(
        provider=provider,
        memory=memory,
        retriever=retriever,
    )

def get_document_service() -> DocumentService:
    return document_service