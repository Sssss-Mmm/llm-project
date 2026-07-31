from llm_backend.models.message import Message
from llm_backend.memories.conversation_memory import ConversationMemory

class InMemoryConversationMemory(ConversationMemory):

    def __init__(self):
        self.messages: dict[str, list[Message]] = {}

    def load(self, conversation_id: str) -> list[Message]:
        return self.messages.get(conversation_id, [])

    def save(self, conversation_id: str, message: Message) -> None:
        if conversation_id not in self.messages:
            self.messages[conversation_id] = []
        self.messages[conversation_id].append(message)

    def clear(self, conversation_id: str) -> None:
        if conversation_id in self.messages:
            del self.messages[conversation_id]