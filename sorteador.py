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
        font-weight: bold;
        color: #4b0082;
        font-size: 25px;
    }
    .stButton button {
        background-color: #6a0dad;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 8px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1>🎉 Sorteador Online 🎉</h1>", unsafe_allow_html=True)

# Entrada de dados
entrada = st.text_area("✍️ Digite os nomes ou números separados por vírgula:")

# Botão de sorteio
if st.button("🎯 Sortear"):
    if entrada.strip():
        itens = [item.strip() for item in entrada.split(",") if item.strip()]
        sorteado = random.choice(itens)
        st.success(f"🥳 O sorteado foi: **{sorteado}**")
    else:
        st.warning("⚠️ Por favor, insira ao menos um item para sortear.")
