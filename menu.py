from flet import *

class Menu(Column):
    # construtor
    def __init__(self):
        super().__init__()
        self.ligar = IconButton(
                    icon=Icons.POWER_SETTINGS_NEW,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                )

        self.desligar = IconButton(
                    icon=Icons.POWER_OFF,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                )
        self.controls = [self.ligar, self.desligar]

