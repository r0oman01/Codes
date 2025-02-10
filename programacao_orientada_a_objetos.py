import datetime as dt

class Conta:
    def __init__(self, nome: str, cpf: str, cel: str, n_conta: str, agencia: str, saldo: float):
        self.__nome = nome
        self.__cpf = cpf
        self.__cel = cel
        self.__n_conta = n_conta
        self.__agencia = agencia
        self.__saldo = saldo
        self.__logg = []  # Lista de logs

    # Getters e Setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def cel(self):
        return self.__cel

    @cel.setter
    def cel(self, cel):
        self.__cel = cel

    @property
    def n_conta(self):
        return self.__n_conta

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

    # Depósito
    def depositar(self, valor: float):
        valor_anterior = self.__saldo
        self.__saldo += valor
        self.__logg.append({
            "operação": "Depósito",
            "valor": valor,
            "data": dt.datetime.today().strftime("%Y-%m-%d"),
            "saldo anterior": valor_anterior,
            "saldo atual": self.__saldo
        })

    # Saque
    def sacar(self, valor: float):
        if self.__saldo >= valor:
            valor_anterior = self.__saldo
            self.__saldo -= valor
            self.__logg.append({
                "operação": "Saque",
                "valor": valor,
                "data": dt.datetime.today().strftime("%Y-%m-%d"),
                "saldo anterior": valor_anterior,
                "saldo atual": self.__saldo
            })
        else:
            print("Saldo insuficiente para o saque.")

    # Setter de saldo, permitiendo alteração apenas se o nome for "Gabriel"
    @saldo.setter
    def saldo(self, saldo):
        if self.nome == "Gabriel":
            self.__saldo = saldo
        else:
            print("Não pode alterar o saldo.")

    # Getter de logg (para exibir as operações realizadas)
    @property
    def logg(self):
        data = ""  # Inicializa a string vazia
        for movimento in self.__logg:
            data += f"""
Operação: {movimento["operação"]} 
Valor: R${movimento["valor"]}
Data: {movimento["data"]}
Saldo anterior: R${movimento["saldo anterior"]}
Saldo atual: R${movimento["saldo atual"]}
----------------------------------
"""
        return data


c1 = Conta("Gabriel", "000.000.000.00", "(11)111111111", "1", "160", 1200)

c1.saldo = 1000
c1.sacar(90)
c1.depositar(500)
c1.sacar(100)
print(c1.logg)
