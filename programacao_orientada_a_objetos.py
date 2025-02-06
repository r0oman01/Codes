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

class Conta:
    def __init__(self, nome, cpf, cel, n_conta, agencia, saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__cel = cel
        self.__n_conta = n_conta
        self.__agencia = agencia
        self.__saldo = saldo

    #getter
    @property
    def nome(self):
        return self.__nome

    #setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    # setter
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def cel(self):
        return self.__cel

    # setter
    @cel.setter
    def cel(self, cel):
        self.__cel = cel

    @property
    def n_conta(self):
        return self.__n_conta

    # setter
    @n_conta.setter
    def n_conta(self, n_conta):
        self.__n_conta = n_conta

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia


    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if self.nome == "Gabriel":
            self.__saldo = saldo
        else:
            print("Não pode alterar")

c1 = Conta("Gabriel", "000.000.000.00", "(11)111111111", "1", "160", 1200)

c1.saldo = 3000
print(c1.saldo)






