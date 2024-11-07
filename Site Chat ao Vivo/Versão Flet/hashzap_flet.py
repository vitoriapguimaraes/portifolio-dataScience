# Hashzap, versão alternativa

import flet as ft

def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        if not nome_usuario.value:
            print("Nome do usuário está vazio!")
            return
        if not campo_mensagem.value.strip():
            print("Mensagem está vazia!")
            return
        pagina.pubsub.send_all({"texto": campo_mensagem.value.strip(), "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        if not nome_usuario.value.strip():
            print("Nome do usuário está vazio!")
            return
        pagina.pubsub.send_all({"usuario": nome_usuario.value.strip(), "tipo": "entrada"})
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem]))
        pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem-vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, port=8000)