from llm_backend.memories.conversation_memory import ConversationMemory
from llm_backend.models.message import Message
from llm_backend.models.role import Role
from llm_backend.provider.llm_provider import LLMProvider


class ChatService:
    def __init__(
        self,
        provider: LLMProvider,
        memory: ConversationMemory,
    ):
        self.provider = provider
        self.memory = memory

    def chat(
        self,
        conversation_id: str,
        message: str,
    ) -> str:

        # 1. 사용자 메시지 생성
        user_message = Message(
            role=Role.USER,
            content=message,
        )

        # 2. 메모리에 저장
        self.memory.save(conversation_id, user_message)

        # 3. 전체 대화 조회
        history = self.memory.load(conversation_id)

        # 4. LLM 호출
        reply = self.provider.chat(history)

        # 5. AI 응답 생성
        assistant_message = Message(
            role=Role.ASSISTANT,
            content=reply,
        )

        # 6. 메모리에 저장
        self.memory.save(conversation_id, assistant_message)

        # 7. 응답 반환
        return reply