import streamlit as st
from crew import PersonagemCrew


def mostrar(personagem):
    nome = personagem[0]
    alias = personagem[1]

    # Título da aplicação
    st.title(nome)

    # Entrada do usuário
    user_input = st.text_input("Pergunta:", "Digite sua pergunta")

    # Botão de envio
    if st.button("Enviar"):
        # Configuração do agente
        inputs = {"pergunta": user_input}
        personagem_crew = PersonagemCrew(alias)
        # Executa a crew
        result = dict(personagem_crew.crew().kickoff(inputs=inputs))

        # Exibe o resultado
        st.write(nome, ":", result["raw"])
