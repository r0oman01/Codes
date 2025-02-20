from cProfile import label

from flet import *
class Bebida(Container):
    def __init__(self):
        super().__init__()
        self.t_fieldNome = TextField(label=Text("Produto", color="black"), color="black")
        self.dropTipo = Dropdown(
        label= Text("Tipo", color="black"),
        width=150,
        border_color="black",
        options=[
            dropdown.Option("Lata"),
            dropdown.Option("Galão"),
            dropdown.Option("Garrafa"),
        ],
    )
        self.dropCategoria = Dropdown(
            label=Text("Categoria", color="black"),
            width=150,
            border_color="black",
            options=[
                dropdown.Option("Coquetel"),
                dropdown.Option("Destilado"),
                dropdown.Option("Água"),
                dropdown.Option("Cerveja"),
            ],
        )
        self.camera = ElevatedButton(text = "Câmera", icon = Icons.CAMERA_ALT)
        self.btnCadastrar = ElevatedButton(text="Cadastrar", icon = Icons.ADD)


        self.tabela = DataTable(

            columns=[
                DataColumn(label=Text("Bebida", color="black")),
                DataColumn(label=Text("Categoria", color="black")),
                DataColumn(label=Text("Tipo", color="black"))

            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(content=Text("Vinho", color="black")),
                        DataCell(content=Text("Destilado", color="black")),
                        DataCell(content=Text("Garrafa", color="black"))
                    ]

                ),
                DataRow(
                    cells=[
                        DataCell(content=Text("Água Mineral", color="black")),
                        DataCell(content=Text("Água", color="black")),
                        DataCell(content=Text("Garrafa", color="black"))
                    ]

                )


            ]
        )


        self.alignment = alignment.top_center
        linha = Row(
            controls=[
                Container(content=self.t_fieldNome),
                Container(content=self.dropTipo),
                Container(content=self.dropCategoria),
                Container(content=self.camera),
                Container(content=self.btnCadastrar),
            ]
        )

        linhaTabela = Row(controls=[self.tabela])
        self.content = Column(controls=[linha, linhaTabela], horizontal_alignment = CrossAxisAlignment.CENTER)