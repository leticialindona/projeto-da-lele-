import streamlit as st

st.title('teste da lele') 
st.write("a lele gosta de unicornios")
st.image("https://github.com/leticialindona/projeto-da-lele-/blob/main/download.jpg?raw=true")
nome = st.text_input('Digite o seu nome')
if nome:
  st.write(nome, 'é muito legal e feliz, ele(a) gosta de unicórnios')

import streamlit as st
import random

st.title("🦄 Mundo dos Unicórnios")
st.write("Descubra curiosidades mágicas!")

curiosidades = [
    "Unicórnios aparecem em mitologias antigas.",
    "Na Idade Média, tinham poderes mágicos.",
    "O unicórnio é símbolo da Escócia.",
    "Representam pureza e força."
]

if st.button("✨ Revelar curiosidade"):
    st.write(random.choice(curiosidades))
