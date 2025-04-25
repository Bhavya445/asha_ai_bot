from main import ChatBot
import streamlit as st

# Initialize the chatbot
bot = ChatBot()

# Set page configuration (streamlit automatically handles the dark/light theme based on user settings)
st.set_page_config(page_title="Asha AI Bot - Empowering Women")

# Sidebar for navigation
with st.sidebar:
    st.title('Asha AI Bot')

    # Quick Links Section
    st.subheader("🔗 Quick Links")
    if st.button("🌟 View Jobs"):
        st.session_state.messages.append({"role": "assistant", "content": "Explore jobs here: https://www.herkey.com/jobs"})

    if st.button("🏢 Explore Companies"):
        st.session_state.messages.append({"role": "assistant", "content": "Check out companies here: https://www.herkey.com/companies"})

    if st.button("📅 Upcoming Events"):
        st.session_state.messages.append({"role": "assistant", "content": "Join events here: https://events.herkey.com/events"})

    if st.button("👭 Connect with Groups"):
        st.session_state.messages.append({"role": "assistant", "content": "Meet like-minded women here: https://www.herkey.com/groups"})

    # Contact Us Section
    st.subheader("📬 Contact Us")
    st.write("For any queries, please contact us at: **info@herkey.com**")

# Function to generate chatbot response
def generate_response(input):
    raw_output = bot.rag_chain.invoke(input)
    print("Model raw output:", repr(raw_output))  # For debugging
    return raw_output

# Initialize session state for messages
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! I'm Asha, here to support your career journey."}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle user input and generate chatbot response
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking about your future..."):
            response = generate_response(input)
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
