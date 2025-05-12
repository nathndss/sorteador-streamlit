import streamlit as st
import random

# CSS customizado
st.markdown("""
<style>
/* Fundo geral */
body, .main {
    background-color: #f5f0ff;
    font-family: 'Segoe UI', sans-serif;
}

.titulo {
    font-size: 56px !important;
    color: #6a0dad;
    text-align: center;
    margin-bottom: 20px;
}
}

#entrada-box textarea {
    font-size: 22px;
    color: #4b0082;
    background-color: #fafafa;
    border: 2px solid #6a0dad;
    border-radius: 8px;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
    width: 100% !important;    /* Aumenta a largura */
    height: 300px !important;  /* Aumenta a altura */
    padding: 15px;
}

#entrada-box textarea:hover,
#entrada-box textarea:focus {
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.15);
    border-color: #9b30ff;
}

/* Botão sorteio */
.stButton > button {
    display: block;
    margin: 5px auto 0 auto;.  /* Reduzido o espaço acima */
    background-color: violet;
    color: violet;
    font-size: 18px;
    padding: 10px 30px;
    border: none;
    border-radius: 10px;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.15);
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.stButton > button:hover {
    background-color: #7b1fa2;
    transform: scale(1.03);
}

/* Resultado */
.resultado {
    text-align: center;
    font-size: 70px;
    color: white;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='titulo'>🎲 Sorteador 🎲</h1>", unsafe_allow_html=True)
# Caixa de entrada
with st.container():
    st.markdown('<div id="entrada-box">', unsafe_allow_html=True)
    entrada = st.text_area("✍️ Digite os nomes ou números separados por vírgula:", height=200)
    st.markdown('</div>', unsafe_allow_html=True)

# Botão de sorteio
if st.button("🎯 Sortear"):
    nomes = [x.strip() for x in entrada.split(",") if x.strip()]
    if nomes:
        sorteado = random.choice(nomes)
        st.markdown(f"<div class='resultado'>✅Resultado: <strong>{sorteado}</strong></div>", unsafe_allow_html=True)
    else:
        st.warning("Por favor, insira pelo menos um nome ou número válido.")


