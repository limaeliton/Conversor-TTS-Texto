# Conversor de Texto para Fala (TTS) 🗣️🎧

Este projeto é um **Conversor de Texto para Fala (TTS)** desenvolvido em Python com uma interface web moderna utilizando Streamlit. Ele permite que os usuários insiram um texto e gerem um arquivo de áudio no formato MP3. 🎵

## Objetivo 🎯

O objetivo deste projeto é facilitar a conversão de textos em áudio, proporcionando uma interface intuitiva e visualmente atraente. Seja para estudos, acessibilidade ou automação, este conversor é uma solução prática e eficiente. 🚀

## Funcionalidades ✨

- Interface web estilizada com Streamlit.
- Entrada de texto personalizada.
- Geração de arquivos de áudio no formato MP3.
- Mensagem de sucesso com fundo escuro para melhor contraste.
- Botão para download do arquivo gerado.

## Como funciona? ⚙️

1. O usuário insere o texto na área de entrada da interface.
2. Ao clicar no botão "Gerar Áudio", o texto é convertido em áudio utilizando a biblioteca `gTTS`.
3. O áudio é processado e exportado no formato MP3 com a ajuda da biblioteca `pydub`.
4. O usuário pode baixar o arquivo gerado diretamente pela interface.

## Requisitos 🛠️

Certifique-se de ter as seguintes dependências instaladas antes de executar o projeto:

- Python 3.6 ou superior 🐍
- Bibliotecas Python:
  - `streamlit`
  - `gTTS`
  - `pydub`
- FFmpeg (necessário para o funcionamento do `pydub`) 🎥

## Como executar? ▶️

1. Clone este repositório ou copie os arquivos para o seu ambiente local. 📂
2. Instale as dependências necessárias:
   ```bash
   pip install streamlit gtts pydub
   ```
3. Certifique-se de que o FFmpeg está instalado e configurado no seu sistema. 🛠️
4. Execute o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```
5. Acesse a interface no navegador pelo endereço exibido no terminal (geralmente `http://localhost:8501`).

## Exemplo de uso 📖

1. Insira um texto como:
   ```
   Python é uma linguagem essencial para análise de dados devido à sua simplicidade e versatilidade.
   ```
2. Clique no botão "Gerar Áudio".
3. Baixe o arquivo gerado clicando no botão "📥 Baixar Áudio".

## Contribuições 🤝

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto. 💡

---

Feito com ❤️ e Python 🐍
