import streamlit as st
from streamlit_app.crew import StreamlitAppCrew

# Título da aplicação
st.title("Aplicação CrewAI com Streamlit")

# Entrada do usuário
user_input = st.text_input("Pergunta:", "Digite sua pergunta")

# Botão de envio
if st.button("Enviar"):
    # Configuração do agente
    inputs = {"pergunta": user_input}

    # Executa a crew
    result = dict(StreamlitAppCrew().crew().kickoff(inputs=inputs))

    # Exibe o resultado
    st.write("Resposta do agente:", result["raw"])
