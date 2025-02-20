from flet import *

class Menu(View):
    # construtor
    def __init__(self):
        super().__init__()
        self.bgcolor="#4285F4"
        rail = NavigationRail(

            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            # extended=True,
            min_width=100,
            min_extended_width=400,
            leading=FloatingActionButton(icon=Icons.LOCAL_DRINK, text="Adcionar"),
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon=Icons.SHOPPING_CART_SHARP, selected_icon=Icons.SHOPPING_CART_SHARP, label="Carrinho"
                ),
                NavigationRailDestination(
                    icon=Icon(Icons.INVENTORY),
                    selected_icon=Icon(Icons.INVENTORY),
                    label="Estoque",
                ),
                NavigationRailDestination(
                    icon=Icons.EXIT_TO_APP,
                    selected_icon=Icon(Icons.EXIT_TO_APP),
                    label_content=Text("Sair"),
                ),

            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
        )

        self.conteudo = Container(content=Text("Página Produto"))

        self.route = "/menu"
        self.body = Row(controls=[rail, self.conteudo], expand=True)
        self.controls = [self.body]
