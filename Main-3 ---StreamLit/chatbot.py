# chatbot.py
import streamlit as st
from openai import OpenAI

# Set page configuration
st.set_page_config(
    page_title="Website Chat Assistant",
    page_icon="🤖",
    layout="centered"
)

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Namaste! Main aapki kya madad kar sakta hoon?"}
    ]

# Sidebar for API key input (alternative to secrets)
with st.sidebar:
    st.title("Chatbot Setup")
    if "OPENAI_API_KEY" in st.secrets:
        st.success("API key loaded!", icon="✅")
    else:
        api_key = st.text_input("Enter OpenAI API key:", type="password")
        if api_key:
            client.api_key = api_key
            st.success("API key saved for this session!", icon="🔑")
    
    st.markdown("[Get OpenAI API key](https://platform.openai.com/account/api-keys)")
    st.divider()
    st.caption("Made with ❤️ using Streamlit")

# Main chat interface
st.title("🤖 Website Chat Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Aapka prashna yahan likhen..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Stream the response
            for response in client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                if response.choices[0].delta.content:
                    full_response += response.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please check your API key or internet connection")