from langchain_groq import ChatGroq
import streamlit as st

# Configuração do Llama
grog_api_key = st.secrets.get("GROQ_API_KEY")

llama_3 = ChatGroq(
    api_key=grog_api_key,
    model="llama3-70b-8192",
    timeout=180,
)
