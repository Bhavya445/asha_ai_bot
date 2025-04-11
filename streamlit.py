from main import ChatBot
import streamlit as st

bot = ChatBot()

st.set_page_config(page_title="Asha AI Bot - Empowering Women")
with st.sidebar:
    st.title('Asha AI Bot')

def generate_response(input):
    return bot.rag_chain.invoke(input)

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! I'm Asha, here to support your career journey."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking about your future..."):
            response = generate_response(input)
            st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
def generate_response(input):
    raw_output = bot.rag_chain.invoke(input)
    print("Model raw output:", repr(raw_output))  # For debugging
    return raw_output
