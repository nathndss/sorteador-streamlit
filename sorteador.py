import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Sorteador Online", page_icon="🎲")

# Estilos personalizados
st.markdown("""
    <style>
    .main {
        background-color: #f5f0ff;
    }
    h1 {
        color: #6a0dad;
        text-align: center;
    }
    .stTextArea label {
        text-align: center;
        font-weight: bold;
        color: #4b0082;
        font-size: 25px;
    }
    .stButton button {
        background-color: #6a0dad;
        color: white;
        font-size: 80px;
        border-radius: 16px;
        padding: 16px 40px;
        position: center;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1>🎉 Sorteador Online 🎉</h1>", unsafe_allow_html=True)

# Entrada de dados
st.markdown("<h3 style='color: white;'>✍️ Digite os nomes ou números separados por vírgula:</h3>", unsafe_allow_html=True)
entrada = st.text_area(label="", height=140)

# Botão de sorteio
col1, col2, col3 = st.columns([1, 2, 1])  # Cria 3 colunas, a do meio é maior

with col2:
    if st.button("🎯 Sortear"):
        if entrada.strip():
            itens = [item.strip() for item in entrada.split(",") if item.strip()]
            sorteado = random.choice(itens)
            st.success(f"🥳 O sorteado foi: **{sorteado}**")
        else:
            st.warning("⚠️ Por favor, insira ao menos um item para sortear.")
