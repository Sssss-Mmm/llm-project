from llm_backend.memories.conversation_memory import ConversationMemory
from llm_backend.models.message import Message
from llm_backend.models.role import Role
from llm_backend.provider.llm_provider import LLMProvider
from llm_backend.retrievers.retriever import Retriever


class ChatService:
    """LLM과의 대화를 관리하는 서비스 클래스이다."""
    def __init__(
        self,
        provider: LLMProvider,
        memory: ConversationMemory,
        retriever: Retriever,
    ):
        """ChatService를 초기화한다."""
        self.provider = provider
        self.memory = memory
        self.retriever = retriever

    def chat(
        self,
        conversation_id: str,
        message: str,
    ) -> str:
        """LLM과의 대화를 수행한다."""
        user_message = Message(
            role=Role.USER,
            content=message,
        )

        self.memory.save(conversation_id, user_message)

        history = self.memory.load(conversation_id)

        documents = self.retriever.retrieve(message)

        reply = self.provider.chat(
            history,
            documents,
        )

        assistant_message = Message(
            role=Role.ASSISTANT,
            content=reply,
        )

        self.memory.save(
            conversation_id,
            assistant_message,
        )

        return reply