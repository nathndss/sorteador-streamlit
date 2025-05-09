import streamlit as st
import random

st.set_page_config(page_title="Sorteador", page_icon="🎲")

st.markdown("<h1 style='text-align: center;  font-size: 28px; color: white;'>🎉 Sorteador Simples 🎉</h1>", unsafe_allow_html=True)

entrada = st.text_area("✍️ Digite os nomes ou números separados por vírgula:")

col1, col2 = st.columns(2)
with col2:
    st.write("Bem-vindo ao sorteador!")
    
if st.button("🎯 Sortear"):
    if entrada.strip():
        itens = [item.strip() for item in entrada.split(",") if item.strip()]
        sorteado = random.choice(itens)
        st.success(f"🥳 O sorteado foi: **{sorteado}**")
    else:
        st.warning("⚠️ Por favor, insira ao menos um item para sortear.")


