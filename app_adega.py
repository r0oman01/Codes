from flet import *
from views.loginView import Login
from views.menuView import Menu
from views.bebidaView import Bebida

def start(page: Page):
    page.title = "Control"

    def changePageMenu(event):
        nome = telaLogin.inputLogin.value
        senha = telaLogin.inputPassword.value

        if not nome and not senha:
            telaLogin.inputLogin.error_text = "Digite um login"
            telaLogin.inputPassword.error_text = "Digite uma senha"
            telaLogin.update()
        else:
            if nome:
                telaLogin.inputLogin.error_text = ""
            else:
                telaLogin.inputLogin.error_text = "Digite um login"

            if senha:
                telaLogin.inputPassword.error_text = ""
            else:
                telaLogin.inputPassword.error_text = "Digite uma senha"

            if nome and senha:
                if nome == "roman" and senha == "123":
                    page.go("/menu")
                    page.update()
                else:
                    telaLogin.inputPassword.error_text = "Senha incorreta"
                    telaLogin.inputLogin.error_text = "Login incorreto"
                    telaLogin.update()

            telaLogin.update()

    telaLogin = Login()

    telaLogin.btnEnter.on_click = changePageMenu
    telaBebida = Bebida()
    telaMenu = Menu(telaBebida)

    def changeRoutes(route):
        if page.route == "/":
            page.views.append(telaLogin)
        elif page.route == "/menu":
            page.views.append(telaMenu)

        page.update()

    page.on_route_change = changeRoutes
    page.go(page.route)

if __name__ == '__main__':
    app(target=start)
