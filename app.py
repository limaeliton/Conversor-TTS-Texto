import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
from googletrans import Translator
import os
import pyttsx3

# Configuração da página (primeiro comando)
st.set_page_config(page_title="Conversor de Texto para Fala", page_icon="🗣️", layout="wide")

# Carrega o Font Awesome para ícones (usado apenas em st.markdown)
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """,
    unsafe_allow_html=True,
)

# Inicializar tradutor
translator = Translator()

# Inicializar chaves no session_state
if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""
if "traducao" not in st.session_state:
    st.session_state["traducao"] = ""

# -- Definições de funções de callback --
def clear_text_callback():
    st.session_state["input_text"] = ""
    st.session_state["traducao"] = ""
    st.session_state["clear_message"] = "Texto limpo com sucesso!"

def editar_traducao_callback():
    traducao = st.session_state.get("traducao", "")
    if traducao and traducao.strip():
        st.session_state["input_text"] = traducao
        st.session_state["edit_message"] = "Texto traduzido movido para edição. Confira o campo com o texto."
    else:
        st.session_state["edit_message"] = "Nenhum texto traduzido disponível para edição."

def reset_interface_callback():
    st.session_state["traducao"] = ""
# -- Fim das funções --

# Estilo personalizado
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e2f;
        font-family: Arial, sans-serif;
    }
    .main-title {
        color: #39ff14;
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
    .menu {
        background-color: #282a36;
        color: #f8f8f2;
        padding: 15px;
        border-radius: 10px;
    }
    .text-input {
        background-color: #282a36;
        color: #f8f8f2;
        border-radius: 5px;
        padding: 10px;
    }
    .text-output {
        background-color: #44475a;
        color: #f8f8f2;
        border-radius: 5px;
        padding: 10px;
    }
    .button {
        background-color: #39ff14;
        color: black;
        font-size: 1rem;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .button:hover {
        background-color: #32cd32;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Layout principal
_ = st.markdown('<h1 class="main-title"><i class="fa fa-comments"></i> Conversor de Texto para Fala 🗣️</h1>', unsafe_allow_html=True)

# Menu lateral com ícones e dicas (sem imagens)
with st.sidebar:
    _ = st.markdown('<div class="menu"><h3><i class="fa fa-bars"></i> Menu</h3></div>', unsafe_allow_html=True)
    idioma = st.selectbox("Escolha o idioma:", ["pt", "en", "es", "fr", "de"], index=0)
    velocidade = st.slider("Velocidade da fala:", 0.5, 2.0, 1.0, step=0.1)
    _ = st.markdown(
        """
        <div class="menu">
            <h4><i class="fa fa-lightbulb"></i> Dicas:</h4>
            <ul>
                <li>Insira textos claros e objetivos.</li>
                <li>Selecione o idioma correto.</li>
                <li>Ajuste a velocidade da fala.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Entrada de texto
_ = st.markdown('<h3 class="sub-title"><i class="fa fa-keyboard"></i> Insira o texto abaixo:</h3>', unsafe_allow_html=True)
texto = st.text_area("Digite o texto aqui:", height=200, placeholder="Escreva algo interessante...", key="input_text")

# Botões principais organizados em colunas
col1, col2, col3 = st.columns(3)

with col1:
    button_traduzir = st.button("Traduzir")
    if button_traduzir:
        if texto.strip():
            try:
                idioma_destino = idioma[:2]
                traducao_obj = translator.translate(texto, dest=idioma_destino)
                if traducao_obj is not None and getattr(traducao_obj, "text", None):
                    st.session_state["traducao"] = traducao_obj.text
                    st.success("Texto traduzido com sucesso!")
                else:
                    st.error("Falha ao obter a tradução. Tente novamente.")
            except Exception as e:
                st.error(f"Erro ao traduzir o texto: {e}")
        else:
            st.error("Por favor, insira um texto para traduzir.")

with col2:
    button_gerar_audio = st.button("Gerar Áudio")
    if button_gerar_audio:
        if texto.strip():
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', velocidade * 200)
                engine.save_to_file(texto, 'audio_pyttsx3.mp3')
                engine.runAndWait()
                st.success("Áudio gerado!")
            except Exception as e:
                st.error(f"Erro ao gerar o áudio: {e}")
        else:
            st.error("Por favor, insira um texto para gerar o áudio.")

with col3:
    st.button("Limpar Texto", key="btn_limpar", on_click=clear_text_callback)

# Botão para resetar a interface (apenas campo de entrada)
if st.button("Nova Tradução", on_click=reset_interface_callback):
    st.success("Interface resetada. Agora, digite o novo texto!")

if "clear_message" in st.session_state:
    st.success(st.session_state["clear_message"])
    del st.session_state["clear_message"]

# Se houver tradução, exibe o resultado e controles adicionais
if "traducao" in st.session_state and st.session_state["traducao"]:
    _ = st.markdown('<h3 class="sub-title"><i class="fa fa-comment-dots"></i> Texto Traduzido:</h3>', unsafe_allow_html=True)
    st.text_area("Texto traduzido:", value=st.session_state["traducao"], height=200, key="translated_text", disabled=True)
    
    # Colunas para gerar áudio traduzido e editar tradução
    col4, col5 = st.columns(2)
    
    with col4:
        button_audio_traduzido = st.button("Gerar Áudio Traduzido")
        if button_audio_traduzido:
            try:
                tts = gTTS(text=st.session_state["traducao"], lang=idioma)
                tts.save("audio_translated.mp3")
                audio = AudioSegment.from_mp3("audio_translated.mp3")
                audio.export("audio_translated_final.mp3", format="mp3")
                st.success("Áudio traduzido gerado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao gerar áudio traduzido: {e}")
    with col5:
        st.button("Editar Tradução", key="btn_edit_trad", on_click=editar_traducao_callback)
    
    if "edit_message" in st.session_state:
        st.info(st.session_state["edit_message"])
        del st.session_state["edit_message"]

# Opção para ouvir o áudio
if st.button("Ouvir Áudio"):
    try:
        if os.path.exists("audio_translated_final.mp3"):
            with open("audio_translated_final.mp3", "rb") as f:
                audio_bytes = f.read()
            st.audio(audio_bytes, format="audio/mp3")
        elif os.path.exists("audio_pyttsx3.mp3"):
            with open("audio_pyttsx3.mp3", "rb") as f:
                audio_bytes = f.read()
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.error("Nenhum áudio disponível para reprodução.")
    except Exception as e:
        st.error(f"Erro ao reproduzir o áudio: {e}")

# Botões para download dos áudios
if os.path.exists("audio_pyttsx3.mp3"):
    with open("audio_pyttsx3.mp3", "rb") as f:
        _ = st.download_button(
            label="Download Áudio",
            data=f.read(),
            file_name="audio_pyttsx3.mp3",
            mime="audio/mp3"
        )
if os.path.exists("audio_translated_final.mp3"):
    with open("audio_translated_final.mp3", "rb") as f:
        _ = st.download_button(
            label="Download Áudio Traduzido",
            data=f.read(),
            file_name="audio_translated_final.mp3",
            mime="audio/mp3"
        )
