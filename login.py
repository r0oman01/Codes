from flet import *

class Login(Column):
    # construtor
    def __init__(self):
        super().__init__()
        self.inputLogin = TextField(label="Login")
        self.inputPassword = TextField(label="Password", password=True)
        self.btnEnter = ElevatedButton(text="Login",width=300, color="green")
        self.controls = [self.inputLogin,self.inputPassword, self.btnEnter]

