import streamlit as st
import random

# CSS customizado para estilo global
st.markdown("""
<style>
/* Fundo geral */
body, .main {
    background-color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Título */
h1 {
    color: #6a0dad;
    text-align: center;
    font-size: 36px;
    margin-bottom: 20px;
}

/* Área de texto personalizada */
#entrada-box textarea {
    font-size: 22px;  /* Tamanho maior do texto */
    color: #4b0082;
    background-color: #fafafa;  /* Cor mais clara */
    border: 2px solid #6a0dad;
    border-radius: 8px;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease, border-color 0.3s ease;
    width: 100%;  /* Largura 100% da tela */
    height: 200px;  /* Maior altura */
    padding: 15px;  /* Espaço interno maior */
}

#entrada-box textarea:hover,
#entrada-box textarea:focus {
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.15);
    border-color: #9b30ff;
}

/* Botão sorteio */
.stButton > button {
    display: block;
    margin: 20px auto;
    background-color: white;
    color: white;
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
    font-size: 24px;
    color: #2e0854;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)


# Título do app
st.markdown("<h1>🎲 Sorteador🎲</h1>", unsafe_allow_html=True)

# Entrada de nomes
with st.container():
    st.markdown('<div id="entrada-box">', unsafe_allow_html=True)
    entrada = st.text_area("✍️ Digite os nomes ou números separados por vírgula:")
    st.markdown('</div>', unsafe_allow_html=True)

# Botão centralizado
if st.button("🎯 Sortear"):
    nomes = [x.strip() for x in entrada.split(",") if x.strip()]
    if nomes:
        sorteado = random.choice(nomes)
        st.markdown(f"<div class='resultado'>✅ Sorteado: <strong>{sorteado}</strong></div>", unsafe_allow_html=True)
    else:
        st.warning("Por favor, insira ao menos um nome ou número válido.")

