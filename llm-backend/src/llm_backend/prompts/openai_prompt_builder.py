from llm_backend.models.document import Document
from llm_backend.models.message import Message
from llm_backend.prompts.prompt_builder import PromptBuilder


class OpenAIPromptBuilder(PromptBuilder):

    def build(
        self,
        messages: list[Message],
        documents: list[Document],
    ) -> list[dict]:

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