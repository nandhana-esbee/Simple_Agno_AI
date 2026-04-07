import streamlit as st
import requests

st.title("Simple Agno AI Chatbot")

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

if "clear_input" not in st.session_state:
    st.session_state.clear_input = False

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Clear input safely before widget is created
if st.session_state.clear_input:
    st.session_state.user_input = ""
    st.session_state.clear_input = False

# Display previous Q&A
for item in st.session_state.history:
    st.write(f"**You:** {item['question']}")
    st.write(f"**AI:** {item['answer']}")
    st.write("---")

# Input form
with st.form("chat_form", clear_on_submit=False):
    user_input = st.text_input("Enter your question:", key="user_input")
    submitted = st.form_submit_button("Send")

if submitted:
    if user_input.strip():
        try:
            with st.spinner("Thinking..."):
                response = requests.post(
                    "http://localhost:8000/chat",
                    params={"query": user_input},
                    timeout=60
                )
                response.raise_for_status()
                data = response.json()
                answer = data.get("response", "No response received.")

        except Exception as e:
            answer = f"⚠️ Error: {str(e)}"

        st.session_state.history.append({
            "question": user_input,
            "answer": answer
        })

        # Ask next rerun to clear input
        st.session_state.clear_input = True
        st.rerun()