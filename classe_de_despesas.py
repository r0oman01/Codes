class Despesas:
    def __init__(self, valor: float, descricao: str, realizado: bool = False):
        self.valor = valor
        self.descricao = descricao
        self.realizado = realizado

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if valor < 0:
            raise ValueError("O valor da despesa não pode ser negativo.")
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if not descricao:
            raise ValueError("A descrição não pode ser vazia.")
        self.__descricao = descricao

    @property
    def realizado(self):
        return self.__realizado

    @realizado.setter
    def realizado(self, realizado: bool):
        self.__realizado = realizado

    def imprimir_despesa(self):
        status = "Realizado" if self.realizado else "Não realizado"
        print(f"\nDespesa: {self.descricao}")
        print(f"Valor: R${self.valor:.2f}")
        print(f"Status: {status}")

    def alterar_status(self, novo_status: bool):
        self.realizado = novo_status
        print(f"Status alterado para: {'Realizado' if novo_status else 'Não realizado'}")

    def realizar_pagamento(self, valor_pago: float):
        if valor_pago < self.valor:
            print(
                f"Pagamento insuficiente. O valor pago (R${valor_pago:.2f}) é menor que o valor da despesa (R${self.valor:.2f}).")
            return False
        else:
            self.realizado = True
            print(f"Pagamento realizado com sucesso! R${valor_pago:.2f} foi pago para a despesa de R${self.valor:.2f}.")
            return True


class Receita:
    def __init__(self, valor: float, descricao: str, recebida: bool = False):
        self.valor = valor
        self.descricao = descricao
        self.recebida = recebida

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if valor < 0:
            raise ValueError("O valor da receita não pode ser negativo.")
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if not descricao:
            raise ValueError("A descrição não pode ser vazia.")
        self.__descricao = descricao

    @property
    def recebida(self):
        return self.__recebida

    @recebida.setter
    def recebida(self, recebida: bool):
        self.__recebida = recebida

    def imprimir_receita(self):
        status = "Recebida" if self.recebida else "Não recebida"
        print(f"\nReceita: {self.descricao}")
        print(f"Valor: R${self.valor:.2f}")
        print(f"Status: {status}")

    def alterar_status(self, novo_status: bool):
        self.recebida = novo_status
        print(f"Status alterado para: {'Recebida' if novo_status else 'Não recebida'}")

    def realizar_recebimento(self, valor_recebido: float):
        if valor_recebido < self.valor:
            print(
                f"Recebimento insuficiente. O valor recebido (R${valor_recebido:.2f}) é menor que o valor da receita (R${self.valor:.2f}).")
            return False
        else:
            self.recebida = True
            print(f"Recebimento realizado com sucesso! R${valor_recebido:.2f} foi recebido para a receita de R${self.valor:.2f}.")
            return True


despesa = Despesas(200.00, "Pagamento de fatura")
print("-"*20)
despesa.imprimir_despesa()

despesa.realizar_pagamento(200.00)

despesa.imprimir_despesa()
print("-"*20)

receita = Receita(1000.00, "Recebimento de pagamento de cliente")

receita.imprimir_receita()

receita.realizar_recebimento(1200.00)

receita.imprimir_receita()
print("-"*20)

