from flet import *
from login import Login
from menu import Menu

def start(page: Page):
    page.title = "Control"

    # Criando o objeto Login()
    def changepagemenu(event):
        nome = tela_login.inputLogin.value
        senha = tela_login.inputPassword.value

        # Verificando se os campos estão preenchidos corretamente
        if nome == "carlos" and senha == "123":
            page.go("/menu")
            page.update()
        else:
            # Se o nome ou a senha estiverem errados, mostramos os erros de forma apropriada
            if nome != "carlos":
                tela_login.inputLogin.error_text = "Login incorreto"
            else:
                tela_login.inputLogin.error_text = ""

            if senha != "123":
                tela_login.inputPassword.error_text = "Senha incorreta"
            else:
                tela_login.inputPassword.error_text = ""

        # Atualiza a tela de login
        tela_login.update()

    tela_login = Login()
    tela_login.btnEnter.on_click = changepagemenu
    tela_menu = Menu()

    def changeroutes(route):
        # Adiciona a tela de login na rota principal
        page.views.append(
            View(route="/", controls=[tela_login])
        )

        # Quando a rota for '/menu', adiciona a tela do menu
        if page.route == "/menu":
            page.views.append(
                View(route="/menu", controls=[tela_menu])
            )
        page.update()

    page.on_route_change = changeroutes
    page.go(page.route)

if __name__ == "__main__":
    app(target=start)
