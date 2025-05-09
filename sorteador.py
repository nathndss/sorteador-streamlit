import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Sorteador Online", page_icon="🎲")

# Estilo personalizado (CSS)
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
        font-size: 30px;
        color: #4b0082;
        background-color: #f0e6ff;
        border: 2px solid #6a0dad;
        border-radius: 8px;
    }
    #entrada-box label {
        font-size: 25px;
        color: #6a0dad;
        font-weight: bold;
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

# Entrada personalizada com CSS
with st.container():
    st.markdown('<div id="entrada-box">', unsafe_allow_html=True)
    entrada = st
