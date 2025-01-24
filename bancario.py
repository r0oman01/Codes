from time import sleep
def listar_contas(conta):
    print("Agência | Tipo | Conta | Saldo | Titular | Cheque Especial")
    print("-"*20)
    for linha in conta:
        print(" | ".join(map(str, linha)), end=" |\n")

def main():
    print("-"*20)
    conta = [
        [791, 1, 12345, 2000, "GA", 1000],
        [893, 2, 98765, 5000, "GR", 2000]
    ]

    while True:
        print("1 - Listar | 2 - Saque | 3 - Depósito | 4 - Sair")
        sleep(1)
        try:
            menu = int(input("Digite o número da opção: "))
            print("-" * 20)

        except ValueError:
            print("Opção inválida. Por favor, escolha um número.")
            continue

        match menu:
            case 1:
                listar_contas(conta)
            case 2:
                try:
                    conta_num = int(input("Digite o número da conta (1 ou 2): ")) - 1
                    if 0 <= conta_num < len(conta):
                        valor_saque = float(input("Digite o valor do saque: "))
                        saldo_disponivel = conta[conta_num][3] + conta[conta_num][5]
                        if valor_saque <= saldo_disponivel:
                            conta[conta_num][3] -= valor_saque
                            print(f"Saque de {valor_saque} realizado com sucesso. Novo saldo: {conta[conta_num][3]}")
                        else:
                            print(f"Saldo insuficiente. Você tem {saldo_disponivel} disponível.")
                    else:
                        print("Número de conta inválido.")
                except (ValueError, IndexError):
                    print("Entrada inválida. Tente novamente.")
            case 3:
                try:
                    conta_num = int(input("Digite o número da conta (1 ou 2): ")) - 1
                    if 0 <= conta_num < len(conta):
                        valor_deposito = float(input("Digite o valor do depósito: "))
                        conta[conta_num][3] += valor_deposito
                        print(f"Depósito de {valor_deposito} realizado com sucesso. Novo saldo: {conta[conta_num][3]}")
                    else:
                        print("Número de conta inválido.")
                except (ValueError, IndexError):
                    print("Entrada inválida. Tente novamente.")
            case 4:
                print("Saindo...")
                sleep(2)
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()
