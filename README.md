# Conversor de Texto para Fala (TTS) 🗣️🎧

Este projeto é um **Conversor de Texto para Fala (TTS)** desenvolvido em Python com uma interface web criada com [Streamlit](https://streamlit.io/). A aplicação permite que o usuário insira um texto, traduza para outro idioma, gere áudios (tanto do texto original quanto do traduzido) e baixe os arquivos MP3 resultantes.

## Objetivo 🎯

Fornecer uma solução prática para converter textos em áudio com funcionalidades adicionais como tradução e edição, facilitando o acesso à informação para estudos, acessibilidade e automação.

## Funcionalidades ✨

- **Entrada de Texto Personalizada:** Insira o texto de sua preferência.
- **Tradução do Texto:** Traduz o texto inserido para o idioma selecionado utilizando a biblioteca `googletrans`.
- **Geração de Áudio Original:** Converte o texto em áudio usando a biblioteca `pyttsx3`.
- **Geração de Áudio Traduzido:** Converte a tradução em áudio utilizando a biblioteca `gTTS` e processa o resultado com `pydub`.
- **Edição e Reset da Interface:** Permite editar a tradução (copiando o conteúdo para o campo de entrada) e resetar a interface para uma nova conversão.
- **Download dos Áudios:** Baixe os arquivos de áudio gerados (tanto os originais quanto os traduzidos).

## Requisitos 🛠️

- **Python 3.6+**  
- **Bibliotecas Python:**
  - `streamlit`
  - `gTTS`
  - `pydub`
  - `googletrans==4.0.0-rc1` *(recomendado)*
  - `pyttsx3`
- **FFmpeg:** Necessário para o funcionamento adequado do `pydub`.

## Instalação e Configuração ▶️

1. **Clone o repositório ou copie os arquivos** para o seu ambiente local:
   ```bash
   git clone <URL_do_repositório>
   cd Conversor-TTS
   ```
2. **Instale as dependências necessárias:**
   ```bash
   pip install streamlit gtts pydub googletrans==4.0.0-rc1 pyttsx3
   ```
3. **Instale e configure o FFmpeg** conforme as instruções do sistema operacional.

## Como Executar o Projeto

Inicie o aplicativo com o comando:
```bash
streamlit run app.py
```
Abra o navegador no endereço exibido (geralmente `http://localhost:8501`) para utilizar a interface.

## Fluxo de Uso 📖

1. **Inserção de Texto:**  
   Na interface, insira o texto desejado na área de entrada.

2. **Tradução (Opcional):**  
   Clique no botão "Traduzir" para converter o texto para o idioma selecionado (disponível no menu lateral).

3. **Geração de Áudio:**  
   - Clique em "Gerar Áudio" para criar uma versão em áudio do texto original (utilizando `pyttsx3`).
   - Se o texto foi traduzido, utilize "Gerar Áudio Traduzido" para criar um áudio da tradução (usando `gTTS`).

4. **Edição e Reset:**  
   - Use o botão "Editar Tradução" para copiar o texto traduzido de volta ao campo de entrada para ajustes.
   - Clique em "Nova Tradução" para limpar a interface e iniciar uma nova conversão.

5. **Download e Reprodução:**  
   Utilize os botões de download para salvar os arquivos MP3 gerados e clique em "Ouvir Áudio" para reproduzir o áudio diretamente na interface.

## Estrutura do Projeto

- **app.py:**  
  Contém o código principal do aplicativo, com:
  - Configuração da página e carregamento do Font Awesome para ícones.
  - Funções de callback para limpar texto, editar tradução e resetar a interface.
  - Implementação da lógica de tradução, geração de áudio e download dos arquivos.
  
- **README.md:**  
  Este documento, que explica o propósito, funcionalidades e como executar o projeto.

## Contribuições 🤝

Contribuições são muito bem-vindas! Caso tenha sugestões de melhoria ou queira reportar problemas, abra uma _issue_ ou envie um _pull request_.

---

Feito com ❤️ e Python 🐍