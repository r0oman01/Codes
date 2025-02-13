from flet import *
from login import Login
from menu import Menu

def start(page: Page):
    page.title = "Control"

    # Criando um objeto do tipo Login
    def changePageMenu(event):
        nome = telaLogin.inputLogin.value
        senha = telaLogin.inputPassword.value

        # Verificando se o nome de usuário e a senha estão vazios
        if not nome and not senha:
            telaLogin.inputLogin.error_text = "Digite um login"
            telaLogin.inputPassword.error_text = "Digite uma senha"
            telaLogin.update()  # Atualiza a tela para mostrar ambos os erros
        else:
            # Se o nome de usuário foi preenchido, limpa o erro do campo de login
            if nome:
                telaLogin.inputLogin.error_text = ""
            else:
                telaLogin.inputLogin.error_text = "Digite um login"

            # Se a senha foi preenchida, limpa o erro do campo de senha
            if senha:
                telaLogin.inputPassword.error_text = ""
            else:
                telaLogin.inputPassword.error_text = "Digite uma senha"

            # Se ambos estiverem preenchidos, verifica se o login está correto
            if nome and senha:
                if nome == "roman" and senha == "123":
                    page.go("/menu")  # Mudando a página para /menu
                    page.update()
                else:
                    telaLogin.inputPassword.error_text = "Senha incorreta"
                    telaLogin.inputLogin.error_text = "Login incorreto"
                    telaLogin.update()  # Atualizando a tela para mostrar os erros

            telaLogin.update()  # Atualiza a tela com as mensagens de erro

    telaLogin = Login()

    # Ação do botão de login
    telaLogin.btnEnter.on_click = changePageMenu
    telaMenu = Menu()

    def changeRoutes(route):
        # Verificando qual página deve ser exibida de acordo com a rota
        if page.route == "/":
            # Página inicial (Login)
            page.views.append(telaLogin)
        elif page.route == "/menu":
            # Página de menu
            page.views.append(View(route="/menu", controls=[telaMenu]))

        page.update()

    # Mudando de rota
    page.on_route_change = changeRoutes
    page.go(page.route)

if __name__ == '__main__':
    app(target=start)
