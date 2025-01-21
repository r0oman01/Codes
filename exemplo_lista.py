from datetime import datetime as dt
from time import sleep
#registro de compras
print("Seja bem-vindo!")

listaCarrinhos = list()

while True:
    print("Opções".center(50,"-"))
    print("""
Cadastrar produtos
1 - Cadastrar
2 - Mostrar compra
3 - Sair
    """)
    menu1 = input("Escolha uma opção:")
    match menu1:
        case "1":
            print("Tela de cadastro das compras".center(50,"-"))
            carrinho = input("Carrinho: ")
            dataCompra = dt.now().today()
            listaCarrinhos.append(carrinho)
            listaCarrinhos.append(dataCompra)
            listaItens = list()
            while True:
                print("Tela de itens")
                print("""
A - Cadastrar item
B - Sair
                """)
                menu2 = input("Digite a opção: ").upper()
                if menu2 == "A":
                    nomeItem = input("Nome do produto")
                    valorItem = float(input("Valor do produto: R$"))
                    item = [nomeItem, valorItem]
                    listaItens.append(item)
                    listaCarrinhos.append(listaItens)
                elif menu2 == "B":
                    break
                else:
                    print("Escolha uma opção válida!")

        case "2":
            print(listaCarrinhos)

        case "3":
            print("Saindo...")
            sleep(2)
            break
