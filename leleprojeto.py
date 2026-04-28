import streamlit as st

st.title('Teste ECMI 2') 
st.write("Esse é o meu texto")
st.image("https://github.com/leticialindona/projeto-da-lele-/blob/main/download.jpg?raw=true")
nome = st.text_input('Digite o seu nome')
if nome:
  st.write(nome, 'é muito legal e feliz')
