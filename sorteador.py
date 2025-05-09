import streamlit as st
import random

st.set_page_config(page_title="Sorteador", page_icon="🎲")

st.markdown("<h1 style='text-align: center; color: white;'>🎉 Sorteador Simples 🎉</h1>", unsafe_allow_html=True)

entrada = st.text_area("✍️ Digite os nomes ou números separados por vírgula:")

if st.button("🎯 Sortear"):
    if entrada.strip():
        itens = [item.strip() for item in entrada.split(",") if item.strip()]
        sorteado = random.choice(itens)
        st.success(f"🥳 O sorteado foi: **{sorteado}**")
    else:
        st.warning("⚠️ Por favor, insira ao menos um item para sortear.")
st.markdown("""
    <style>
    .stTextArea label {
        font-size: 30px;
        color: #6a0dad;
    }
    .stButton button {
        background-color: #6a0dad;
        color: white;
        font-size: 25px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

