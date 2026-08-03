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
        """주어진 메시지를 기반으로 LLM과 대화를 수행한다."""
        history = self.memory.load(conversation_id)

        user_message = Message(
            role=Role.USER,
            content=message,
        )

        history.append(user_message)

        documents = self.retriever.retrieve(
            query=message,
            top_k=5,
        )

        reply = self.provider.chat(
            history,
            documents,
        )

        self.memory.save(
            conversation_id,
            user_message,
        )

        self.memory.save(
            conversation_id,
            Message(
                role=Role.ASSISTANT,
                content=reply,
            ),
        )

        return reply