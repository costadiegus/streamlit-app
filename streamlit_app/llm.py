import streamlit as st

# Configuração do Llama
grog_api_key = st.secrets.get("GROQ_API_KEY")

llama_3 = "groq/llama3-70b-8192"
