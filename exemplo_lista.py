from datetime import datetime as dt
from time import sleep

# Registro de compras
print("Seja bem-vindo!")
listaCarrinhos = list()


def somar_valores():
    total = 0
    for carrinho in listaCarrinhos:
        for item in carrinho:
            total += item[1]
    return total


while True:
    print("Opções".center(50, "-"))
    print("""
Cadastrar produtos
1 - Cadastrar
2 - Mostrar compra
3 - Mostrar total
4 - Sair
    """)

    menu1 = input("Escolha uma opção: ")

    match menu1:
        case "1":
            print("Tela de cadastro das compras".center(50, "-"))
            carrinho = input("Carrinho: ")
            listaItens = list()

            while True:
                print("Tela de itens")
                print(""" 
A - Cadastrar item
B - Sair
                """)
                menu2 = input("Digite a opção: ").upper()

                if menu2 == "A":
                    nomeItem = input("Nome do produto: ")
                    valorItem = float(input("Valor do produto: R$"))
                    marcaItem = input("Marca do produto: ")
                    item = [nomeItem, valorItem, marcaItem]
                    listaItens.append(item)
                elif menu2 == "B":
                    listaCarrinhos.append(listaItens)
                    break
                else:
                    print("Escolha uma opção válida!")

        case "2":
            for carrinho in listaCarrinhos:
                print("Itens no carrinho:")
                for item in carrinho:
                    print(f"Produto: {item[0]}, Marca: {item[2]}, Valor: R${item[1]:.2f}")

        case "3":
            total = somar_valores()
            print(f"Total de compras: R${total:.2f}")

        case "4":
            print("Saindo...")
            sleep(2)
            break
