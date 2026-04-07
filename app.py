import streamlit as st
import requests

st.title("AI Agent")

query = st.text_input("Ask anything")

if st.button("Send"):
    res = requests.post(
        "http://localhost:8000/chat",
        params={"query": query}
    )
    st.write(res.json()["response"])