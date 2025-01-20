from time import sleep

print("sistema de registro de roupas".upper())

pecas = []
tamanhos = []
valores = []

while True:
    print("""
Escolha a sua opção:
1 - Cadastrar
2 - Mostrar roupas cadastradas
3 - Sair
    """)
    menu1 = input("Escolha a sua opção: ")
    match menu1:
        case "1":
            peca = input("Qual peça de roupa que será cadastrada: ").capitalize()
            tamanho = input("Tamanho da peça: ").upper()
            valor = int(input("Valor da peça: "))

            if (tamanho == "P") or (tamanho == "M") or (tamanho == "G"):
                print("Peça registrada com sucesso!")
            else:
                print("Tamanho incorreto")

            pecas.append(peca)
            tamanhos.append(tamanho)
            valores.append(valor)


        case "2":
            for x in range(len(pecas)):
                if (tamanho == "P") or (tamanho == "M") or (tamanho == "G"):
                    print(f"Peça: {pecas[x]}. Tamanho: {tamanhos[x]}. Valor: R${valores[x]}  ")
                else:
                    break

        case "3":
            print("Saindo...")
            sleep(2)
            break
