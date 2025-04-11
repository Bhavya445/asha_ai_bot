from langchain import PromptTemplate


template = """
Answer the user's question using only the provided context.
Do not include any instructions, prompt text, or greetings in your answer.

Context:
{context}

Question: {question}

Answer in 1–2 concise sentences:
"""


prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)
