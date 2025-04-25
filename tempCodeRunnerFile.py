from dotenv import load_dotenv

from rag_chain import rag_chain

class ChatBot():
    def __init__(self):
        load_dotenv()
        self.rag_chain = rag_chain

# Testing CLI
if __name__ == "__main__":
    bot = ChatBot()
    input_text = input("Ask me anything: ")
    result = bot.rag_chain.invoke(input_text)
    print(result)
