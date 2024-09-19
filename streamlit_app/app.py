import streamlit as st
import persona

# Dicionário contendo os universos e seus respectivos personagens
universos = {
    "DC Comics": [
        ["Eobard Thawne", "eobard_thawne"],
    ],
    "Marvel": [
        ["Prof. Xavier", "xavier"],
    ],
    "Star Wars": [
        ["Mestre Yoda", "yoda"],
        ["Luke Skywalker", "luke_skywalker"],
        ["Rey", "rey"],
    ],
}

# Menu lateral para a escolha do Universo
st.sidebar.title("Menu de Universos e Personagens")

# Primeira combobox para escolher o Universo
universo_selecionado = st.sidebar.selectbox(
    "Escolha o Universo:",
    list(universos.keys()),  # Mostra os nomes dos universos como opções
)

# Verifica se um Universo foi selecionado
if universo_selecionado:
    # Obter apenas os nomes dos personagens (primeiro item de cada lista)
    personagens_nomes = ["Selecione um personagem"] + [
        personagem[0] for personagem in universos[universo_selecionado]
    ]

    # Segunda combobox para escolher o personagem, com base no Universo selecionado
    personagem_selecionado = st.sidebar.selectbox(
        "Escolha o Personagem:",
        personagens_nomes,  # Mostra apenas os nomes dos personagens
    )

    # Verifica se o usuário selecionou um personagem diferente de "Selecione um personagem"
    if personagem_selecionado != "Selecione um personagem":
        st.title(f"{personagem_selecionado}")
        personagem_info = next(
            personagem
            for personagem in universos[universo_selecionado]
            if personagem[0] == personagem_selecionado
        )

        st.write(
            f"Você escolheu {personagem_info[0]} do universo {universo_selecionado}!"
        )
        persona.mostrar(personagem_info)
    else:
        st.write("Por favor, selecione um personagem.")
