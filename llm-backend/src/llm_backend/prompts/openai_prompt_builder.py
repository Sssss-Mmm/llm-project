from llm_backend.models.document import Document
from llm_backend.models.message import Message
from llm_backend.prompts.prompt_builder import PromptBuilder


class OpenAIPromptBuilder(PromptBuilder):
    """OpenAI API에 맞는 프롬프트를 생성하는 Builder 클래스이다."""
    def build(
        self,
        messages: list[Message],
        documents: list[Document],
    ) -> list[dict]:
        """OpenAI API에 맞는 프롬프트를 생성한다."""
        prompt = []

        if documents:

            context = "\n\n".join(
                document.content
                for document in documents
            )

            prompt.append({
                "role": "system",
                "content": f"""
아래 문서를 참고하여 답변하세요.

{context}

문서에 없는 내용은 추측하지 마세요.
"""
            })

        for message in messages:

            prompt.append({
                "role": message.role.value,
                "content": message.content,
            })

        return prompt