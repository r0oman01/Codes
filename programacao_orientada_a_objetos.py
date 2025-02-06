# marca
# modelo
# placa
# cor
# ano
# km
# p_motor
# cambio


class Animal:
    # Construtor da classe
    def __init__(self, especie, cor, tipo, alimentacao):
        self.especie = especie
        self.cor = cor
        self.tipo = tipo
        self.alimentacao = alimentacao
        self.status = ""

    def locomover(self):
        if self.especie == "Panthera leo":
            self.status = "Correr"
        elif self.especie == "Canis rufus":
            self.status = "Correr"
        elif self.especie == "Agnatha":
            self.status = "Nadar"
        else:
            self.status = "Deslocando-se"

        return self.status

a1 = Animal(especie="Panthera leo", cor="Branco", tipo="Terrestre", alimentacao= "Carnívoro")
a2 = Animal(especie="Canis rufus", cor="Cinza", tipo="Terrestre", alimentacao= "Carnívoro")
a3 = Animal(especie="Agnatha", cor="Cinza", tipo="Aquático", alimentacao= "Herbívoro")

print(a1.especie, a1.cor, a1.tipo, a1.alimentacao, a1.locomover())
print(a2.especie, a2.cor, a2.tipo, a2.alimentacao, a2.locomover())
print(a3.especie, a3.cor, a3.tipo, a3.alimentacao, a3.locomover())








