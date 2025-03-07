# FitBot
<br> !!projeto em andamento!! </br>
**FitBot** é um bot para WhatsApp desenvolvido para ajudar você e seus amigos a registrar e compartilhar atividades físicas. Com o **FitBot**, você pode enviar mensagens ao WhatsApp com informações sobre seus treinos e visualizar essas informações de forma organizada em um app. 

Atualmente, o bot filtra mensagens que começam com a palavra-chave **"fitbot"** e armazena as informações no banco de dados **MongoDB**. A plataforma de backend é hospedada no **Vercel** e a comunicação com o WhatsApp é feita usando a **WhatsApp Cloud API**.

## Funcionalidades

- Envio de mensagens pelo WhatsApp contendo informações sobre treinos.
- Armazenamento das mensagens no banco de dados MongoDB.
- Visualização das informações de treinos e atividades em uma interface web (planejada para futuras versões).
- Notificações no grupo de WhatsApp quando um novo check-in de treino é registrado.

## Estrutura do Projeto

Este repositório contém o código do **backend** do FitBot, que processa as mensagens enviadas para o número de WhatsApp configurado e armazena as informações no MongoDB.

### 1. Clone este repositório:

```bash
git clone https://github.com/gabrielaschmitt/fitbot.git
