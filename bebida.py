from flet import *
class Bebida(Container):
    def __init__(self):
        super().__init__()
        self.t_fieldNome = TextField(label="Produto")
        self.dropTipo = Dropdown(
        width=150,
        options=[
            dropdown.Option("Lata"),
            dropdown.Option("Galão"),
            dropdown.Option("Garrafa"),
        ],
    )
        self.dropCategoria = Dropdown(
            width=150,
            options=[
                dropdown.Option("Coquetel"),
                dropdown.Option("Destilado"),
                dropdown.Option("Água"),
                dropdown.Option("Cerveja"),
            ],
        )
        self.camera = ElevatedButton(icon = Icons.CAMERA_ALT)
        self.btnCadastrar = ElevatedButton(text="Cadastrar", icon = Icons.ADD)

        linha = ResponsiveRow()