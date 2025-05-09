import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Sorteador Online", page_icon="🎲")

# Estilo CSS personalizado
st.markdown("""
    <style>
    .main {
        background-color: #f5f0ff;
    }
    h1 {
        color: #6a0dad;
        text-align: center;
    }
    #entrada-box textarea {
        font-size: 18px;
        color: #4b0082;
        background-color: #f0e6ff;
        border: 2px solid #6a0dad;
        border-radius: 8px;
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

# Título da entrada com tamanho e cor personalizada
st.markdown("<h3 style='color: white;'>✍️ Digite os nomes ou números separados por vírgula:</h3>", unsafe_allow_html=True)

# Entrada de texto estilizada
st.markdown('<div id="entrada-box">', unsafe_allow_html=True)
entrada = st.text_area(label="", height=150)
st.markdown('</div>', unsafe_allow_html=True)

# Botão centralizado
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    sortear = st.button("🎯 Sortear")

# Verifique o botão fora da coluna
if 'sortear' in locals() and sortear:
    if entrada.strip():
        itens = [item.strip() for item in entrada.split(",") if item.strip()]
        sorteado = random.choice(itens)
        st.success(f"🥳 O sorteado foi: **{sorteado}**")
    else:
        st.warning("⚠️ Por favor, insira ao menos um item para sortear.")

