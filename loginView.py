from tkinter.constants import CENTER

from flet import Image
from flet import *


class Login(View):
    # construtor
    def __init__(self):
        super().__init__()
        self.inputLogin = TextField(label=Text("Usuário", color="black"), width=300, border_color="black", border_radius=50, color='black', cursor_color="black")
        self.inputPassword = TextField(label=Text("Senha", color="black"), password=True, width=300, border_color="black", border_radius=50, color='black', cursor_color="black")
        self.btnEnter = ElevatedButton(text="Login",width=300, color="green", scale=1)
        imagem = ResponsiveRow(
            controls=[
                Container(content=Image(src="assets/imagem_estranha.jpg"), col={"xs":12, "md":6, "lg":4})
            ], alignment=MainAxisAlignment.CENTER

        )
        linha = ResponsiveRow(controls=[

            Container(content=self.inputLogin, col={"xs":12,"md":6, "lg":4})

        ], alignment=MainAxisAlignment.CENTER)

        linha2 = ResponsiveRow(controls=[

            Container(content=self.inputPassword, col={"xs": 12, "md": 6, "lg": 4})
        ], alignment=MainAxisAlignment.CENTER)

        linha3 = ResponsiveRow(controls=[

            Container(content=self.btnEnter, col={"xs": 12, "md": 6, "lg": 4})
        ], alignment=MainAxisAlignment.CENTER)

        self.route = "/"
        self.controls =  [linha, linha2, linha3, imagem]
        self.bgcolor="white"
