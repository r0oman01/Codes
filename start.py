from flet import  *
from login import Login
from menu import Menu

def start(page:Page):
    page.title = "Control"

    #criando o objeto Login()
    def changepagemenu(event):
        nome = tela_login.inputLogin.value
        senha = tela_login.inputPassword.value
        if nome and senha:
            if nome == "carlos" and senha == "123":
                page.go("/menu")
                page.update()
            else:
                tela_login.inputPassword.error_text = "Digite a senha"
                tela_login.inputLogin.error_text = "Digite o login"

        else:
            tela_login.inputPassword.error_text = "Digite a senha" if not senha else""
            tela_login.inputLogin.error_text="Digite o login" if not nome else""
        tela_login.update()

    tela_login = Login()
    tela_login.btnEnter.on_click= changepagemenu
    tela_menu = Menu()
    def changeroutes(route):
        # append adiciona um objeto view(tela)
        page.views.append(
            View(route = "/", controls=[tela_login])

        )
        #perguntar se estou em outra rota

        if page.route == "/menu":
            page.views.append(
                View(route="/menu", controls=[tela_menu])

            )
        page.update()


    page.on_route_change = changeroutes
    page.go(page.route)

if __name__ == "__main__":
    app(target=start)
