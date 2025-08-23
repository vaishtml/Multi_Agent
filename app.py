import streamlit as st
from agents import MasterAgent
import time

# --- UI CONFIGURATION ---
# Set page title and layout
st.set_page_config(
    page_title="Multi-Agent Chat App",
    layout="wide",
)

# Set the background color for a dark theme
st.markdown(
    """
    <style>
        .reportview-container {
            background: #111;
            color: #fff;
        }
        .stButton>button {
            color: #fff;
            background-color: #333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CHAT HEADER ---
# Add a title and a simple subheader
st.title("🤖 Multi-Agent Chat Playground")
st.markdown("Ask me to do things like math, get weather, or manipulate text.")

# --- AGENT INITIALIZATION & CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "master_agent" not in st.session_state:
    st.session_state.master_agent = MasterAgent()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CHAT INPUT & LOGIC ---
if prompt := st.chat_input("What is up?"):
    # Append and display user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent's response with a spinner
    with st.spinner("Thinking..."):
        time.sleep(1)
        response = st.session_state.master_agent.route_query(prompt)

    # Display agent's response and append it to history
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- SIDEBAR & OPTIONS ---
with st.sidebar:
    st.button("Clear Chat", on_click=lambda: st.session_state.clear())
    #list down all the things the agent can do
    st.markdown("### Capabilities")
    st.markdown("""
    - Basic arithmetic operations 
    - Weather information retrieval for a specified city
    - String manipulations 
    - Unit conversions
    """)
    st.markdown("---")
    