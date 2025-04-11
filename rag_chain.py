from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from vector_store import docsearch
from prompt_template import prompt
from llm_setup import llm




class CleanOutputParser(StrOutputParser):
    def parse(self, text: str) -> str:
        # Remove everything before "Answer in 1–2 concise sentences:" if present
        if "Answer in 1–2 concise sentences:" in text:
            text = text.split("Answer in 1–2 concise sentences:")[-1]

        # Clean further
        text = text.strip()
        lines = text.splitlines()
        clean_lines = [line.strip() for line in lines if line.strip() and not line.lower().startswith(("hello", "hi", "answer the user"))]

        return clean_lines[0] if clean_lines else text


rag_chain = (
    {"context": docsearch.as_retriever(), "question": RunnablePassthrough()}
    | prompt
    | llm
    | CleanOutputParser()
)