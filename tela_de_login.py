from flet import (Page, TextField, ElevatedButton, Text, Row, app, Column, Image, MainAxisAlignment, Icon, Icons)
def main(page: Page):
    #componentes
    page.title = "Login"
    img = Image(src="img_login.png")
    page.bgcolor = "#4B0082"
    usuario = TextField(label="Digite seu usuário")
    senha  = TextField(label="Digite sua senha",password=True)
    btnLogin = ElevatedButton(text="Login", width=300, color="green")
    icon_login = Icon(Icons.LOGIN)
    icon_pass = Icon(Icons.PASSWORD)

    #linhas
    linha0 = Row(controls=[img], alignment=MainAxisAlignment.CENTER)
    linha1 = Row(controls = [icon_login,usuario], alignment=MainAxisAlignment.CENTER)
    linha2 = Row(controls = [icon_pass,senha], alignment=MainAxisAlignment.CENTER)
    linha3 = Row(controls = [btnLogin], alignment=MainAxisAlignment.CENTER)

    coluna = Column(controls = [linha0, linha1, linha2, linha3])


    #atualização
    page.add(coluna)
    page.update()

if __name__ == "__main__":
    app(main, assets_dir="assets")

