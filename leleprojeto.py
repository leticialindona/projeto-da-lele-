import streamlit as st

st.title('teste da lele') 
st.write("a lele gosta de unicornios")
st.image("https://github.com/leticialindona/projeto-da-lele-/blob/main/download.jpg?raw=true")
nome = st.text_input('Digite o seu nome')
if nome:
  st.write(nome, 'é muito legal e feliz, ele(a) gosta de unicórnios')
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Projeto da Lele </title>

  <style>
    body {
      text-align: center;
      font-family: Arial, sans-serif;
      background: linear-gradient(to right, #ffe6f0, #e6ccff);
      margin: 0;
      padding: 
    {

    h1 {
      color: purple;
      font-size: 40px;
    }

    p {
      font-size: 18px;
    }

    button {
      padding: 12px 20px;
      background-color: pink;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 16px;
      margin-top: 20px;
    }

    button:hover {
      background-color: #ffb3d9;
    }

    #curiosidade {
      margin-top: 20px;
      font-weight: bold;
      color: #5a005a;
    }
  </style>
</head>

<body>

  <h1>Mundo dos Unicórnios</h1>
  <p>Descubra curiosidades mágicas sobre unicórnios!</p>

  <button onclick="mostrarCuriosidade()">✨ Revelar curiosidade</button>

  <p id="curiosidade"></p>

  <script>
    const curiosidades = [
      "Unicórnios aparecem em mitologias antigas da Índia e da China.",
      "Na Idade Média, acreditava-se que seus chifres tinham poderes mágicos.",
      "O unicórnio é o animal nacional da Escócia.",
      "Eles simbolizam pureza e força."
    ];

    function mostrarCuriosidade() {
      const aleatorio = Math.floor(Math.random() * curiosidades.length);
      document.getElementById("curiosidade").innerText = curiosidades[aleatorio];
    }
  </script>

</body>
</html>
