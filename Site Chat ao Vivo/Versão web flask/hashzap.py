#  Criar um Chat ao Vivo => HashZap
# Uma espécie de Whatsapp. Vai ser um chat ao vivo, onde as pessoas podem entrar
# e conversar como se fosse um chat normal.

# Resultado do programa:
# Agora você pode abrir o seu chat e conversar com as pessoas que estão
# conectadas a mesma rede que você. Pode inclusive, abrir mais de um chat no
# mesmo computador para verificar que está tudo funcionando normalmente.

# Imports
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Criação do site e do chat
app = Flask(__name__)
app.config["SECRET_KEY"] = "ajuiahfa78fh9f78shfs768fgs7f6"
app.config["DEBUG"] = True # para testarmos o código, no final tiramos
socketio = SocketIO(app, cors_allowed_origins="*")

# Função para executar as mensagens
@socketio.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)

@app.route("/")
def home():
    return render_template("index_formatado.html")

if __name__ == "__main__":
    socketio.run(app, host='localhost')