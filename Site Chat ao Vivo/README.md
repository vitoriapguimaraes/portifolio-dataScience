# HashZap: Chat em Tempo Real
HashZap é um chat ao vivo que permite que usuários conversem em tempo real. Ele simula o funcionamento básico de um aplicativo de mensagens, onde várias pessoas podem participar de uma sala de chat compartilhada e enviar mensagens visíveis para todos os conectados.

## Funcionalidades Gerais
- Envio e recebimento de mensagens em tempo real.
- Transmissão de mensagens para todos os participantes do chat.
- Registro de entrada de novos usuários na sala de chat.
- Interface alternativa em Flet para uma experiência simplificada.

## Ferramentas e Tecnologias Utilizadas
- Python
- Flask: Estrutura principal do servidor.
- Flask-SocketIO: Protocolo de comunicação em tempo real.
- HTML e JavaScript: Para criar a interface de chat e enviar mensagens ao servidor.
- Flet: Alternativa para interface em uma aplicação web simples.

## Como Executar o Chat
1. Instale as dependências:
``` python
pip install -r requirements.txt.
```
2. Executar a versão principal (Flask e SocketIO):
``` python
python app.py
```
Acesse http://localhost:8000 para abrir o chat.
3. Executar a versão alternativa (Flet):
``` python
python flet_version.py
```

## Resultados
Agora você pode abrir o chat e enviar mensagens visíveis para todos os conectados. Para validar o funcionamento, abra múltiplas janelas ou dispositivos conectados à mesma rede e participe do chat em tempo real.