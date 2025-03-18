import streamlit as st
from gtts import gTTS
from pydub import AudioSegment

# Configuração da página
st.set_page_config(page_title="Conversor de Texto para Fala", page_icon="🗣️", layout="centered")

# Estilo da interface
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .main-title {
        color: #4a90e2;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
    }
    .sub-title {
        color: #7f8c8d;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 20px;
    }
    .button {
        background-color: #4a90e2;
        color: white;
        font-size: 1rem;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .button:hover {
        background-color: #357ab8;
    }
    .success-message {
        background-color: #2c3e50;
        color: white;
        padding: 10px;
        border-radius: 5px;
        font-size: 1rem;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Títulos
st.markdown('<h1 class="main-title">Conversor de Texto para Fala 🗣️</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Insira o texto abaixo e gere um arquivo de áudio em MP3.</p>', unsafe_allow_html=True)

# Entrada de texto
texto = st.text_area("Digite o texto aqui:", height=200, placeholder="Escreva algo interessante...")

# Botão para gerar o áudio
if st.button("Gerar Áudio", key="generate_audio"):
    if texto.strip():
        # Gerar o áudio
        tts = gTTS(text=texto, lang='pt-br')
        tts.save('audio_raw.mp3')

        # Converter para o formato final
        audio = AudioSegment.from_mp3('audio_raw.mp3')
        audio.export('audio.mp3', format='mp3')

        # Exibir mensagem de sucesso e link para download
        st.markdown('<div class="success-message">Arquivo de áudio gerado com sucesso! 🎉</div>', unsafe_allow_html=True)
        with open("audio.mp3", "rb") as file:
            st.download_button(
                label="📥 Baixar Áudio",
                data=file,
                file_name="audio.mp3",
                mime="audio/mpeg",
            )
    else:
        st.error("Por favor, insira um texto antes de gerar o áudio.")
