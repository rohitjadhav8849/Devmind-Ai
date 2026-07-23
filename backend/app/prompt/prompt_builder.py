class PromptBuilder:

    @staticmethod
    def build(question: str, chunks: list[str]) -> str:
        context = "\n\n".join(chunks)

        prompt = f"""
You are an Enterprise AI Assistant.

Answer ONLY using the context below.

If the answer is not present in the context,
say "I don't know based on the provided documents."

======================
CONTEXT
======================

{context}

======================
QUESTION
======================

{question}

======================
ANSWER
======================
"""

        return prompt.strip()