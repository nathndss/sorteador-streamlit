import streamlit as st
import random

st.title("Sorteador Simples")

entrada = st.text_area("Digite os nomes ou números separados por vírgula:", "")

if st.button("Sortear"):
    if entrada.strip():
        itens = [item.strip() for item in entrada.split(",") if item.strip()]
        sorteado = random.choice(itens)
        st.success(f"O sorteado foi: **{sorteado}**")
    else:
        st.warning("Por favor, insira pelo menos um item para sortear.")
