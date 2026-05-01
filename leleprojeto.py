import streamlit as st

st.title('teste da lele') 
st.write("a lele gosta de unicornios")
st.image("https://github.com/leticialindona/projeto-da-lele-/blob/main/download.jpg?raw=true")
nome = st.text_input('Digite o seu nome')
if nome:
  st.write(nome, 'é muito legal e feliz, ele(a) gosta de unicórnios')
import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Projeto da Lele 🦄", layout="centered")

# Estilo (equivalente ao CSS)
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffe6f0, #e6ccff);
    }
    .titulo {
        text-align: center;
        color: purple;
        font-size: 40px;
    }
    .texto {
        text-align: center;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Título (equivalente ao <h1>)
st.markdown('<p class="titulo">🦄 Mundo dos Unicórnios</p>', unsafe_allow_html=True)

# Texto
st.markdown('<p class="texto">Descubra curiosidades mágicas sobre unicórnios!</p>', unsafe_allow_html=True)

# Lista de curiosidades (igual ao JS)
curiosidades = [
    "Unicórnios aparecem em mitologias antigas da Índia e da China.",
    "Na Idade Média, acreditava-se que seus chifres tinham poderes mágicos.",
    "O unicórnio é o animal nacional da Escócia.",
    "Eles simbolizam pureza e força."
]

# Botão (equivalente ao onclick)
if st.button("✨ Revelar curiosidade"):
    curiosidade = random.choice(curiosidades)
    st.success(curiosidade)
    st.balloons()



pip install streamlit
streamlit run leleprojeto.py
