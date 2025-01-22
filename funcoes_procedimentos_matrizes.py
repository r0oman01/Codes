
# #criar a função
# def ola(nome, idade):
#     print(f"Seu nome é {nome} e a sua idade é {idade}")
#
#
# ola("Gabriel", 21)
#
# def soma(x,y):
#     return x + y
#
# print(f"A soma dos valores x e y é: {soma(21,43)}")

#matrizes
from time import sleep
linha = int
coluna = int
matriz = []
n1 = []
n2 = []
n3 = []
n4 = []
n5 = []
n6 = []
while True:
    print("""
1 - Cadastrar matriz
2 - Sair
""")
    menu1 = int(input("Digite a opção escolhida: "))
    match menu1:
        case 1:
            n1 = int(input("Digite o primeiro valor da matriz: "))
            n2 = int(input("Digite o segundo valor da matriz: "))
            n3 = int(input("Digite o terceiro valor da matriz: "))
            n4 = int(input("Digite o quarto valor da matriz: "))
            n5 = int(input("Digite o quinto valor da matriz: "))
            n6 = int(input("Digite o sexto valor da matriz: "))

            matriz.append(n1)
            matriz.append(n2)
            matriz.append(n3)
            matriz.append(n4)
            matriz.append(n5)
            matriz.append(n6)

            print("""
1 - Mostrar matriz
2 - Sair
            """)
            menu2 = int(input("Digite a opção escolhida: "))
            match menu2:
                case 1:
                    for linha in matriz:
                        matriz = [
                            [n1,n2,n3],
                            [n4,n5,n6]
                        ]
                        print(matriz)
                        break
                case 2 :
                    print("Saindo...")
                    sleep(2)
                    break
        case 2:
            print("Saindo...")
            sleep(2)
            break




