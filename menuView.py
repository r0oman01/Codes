from flet import *

class Menu(View):
    # construtor
    def __init__(self, telaBebida):
        super().__init__()
        self.bgcolor="white"
        rail = NavigationRail(

            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=FloatingActionButton(icon=Icons.LOCAL_DRINK, text="Bebida"),
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon=Icons.SHOPPING_BAG_OUTLINED, selected_icon=Icons.SHOPPING_BAG_ROUNDED, label="Carrinho"
                ),
                NavigationRailDestination(
                    icon=Icon(Icons.INVENTORY),
                    selected_icon=Icon(Icons.INVENTORY),
                    label="Estoque",
                ),

                NavigationRailDestination(
                    icon=Icons.LIGHTBULB_OUTLINED,
                    selected_icon=Icon(Icons.LIGHTBULB),
                    label_content=Text("Làmpada"),
                ),

                NavigationRailDestination(
                    icon=Icons.DOOR_FRONT_DOOR_OUTLINED,
                    selected_icon=Icon(Icons.DOOR_FRONT_DOOR_ROUNDED),
                    label_content=Text("Porta"),
                ),

                NavigationRailDestination(
                    icon=Icons.CAMERA_ALT_OUTLINED,
                    selected_icon=Icon(Icons.CAMERA_ALT_ROUNDED),
                    label_content=Text("Porta"),
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
        self.body = Row(controls=[rail, telaBebida], expand=True)
        self.controls = [self.body]
