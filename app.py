# import streamlit as st
# import requests

# st.title("Sample Agno Chatbot")

# query = st.text_input("Ask anything")

# if st.button("Send"):
#     res = requests.post(
#         "http://localhost:8000/chat",
#         params={"query": query}
#     )
#     st.write(res.json()["response"])

import streamlit as st
import requests

st.title("Simple Agno AI Chatbot")

# Store conversation
if "history" not in st.session_state:
    st.session_state.history = []

# Display previous Q&A
for item in st.session_state.history:
    st.write("**You:**", item["question"])
    st.write("**AI:**", item["answer"])
    st.write("---")

# Input at bottom
user_input = st.text_input("Enter your question:")

if st.button("Send"):
    if user_input.strip() != "":
        try:
            response = requests.post(
                "http://localhost:8000/chat",
                params={"query": user_input}
            )

            answer = response.json().get("response")

        except Exception as e:
            answer = f"⚠️ Error: {str(e)}"

        # Save to history
        st.session_state.history.append({
            "question": user_input,
            "answer": answer
        })

        # Clear input
        st.rerun()