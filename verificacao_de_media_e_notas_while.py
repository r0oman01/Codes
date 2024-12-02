from datetime import time
from time import sleep

print("---Sistema de cadastro de pessoas---".upper())
n1: float = 0
n2: float = 0
n3: float = 0
n4: float = 0
while True:
    print("---sejam bem-vindos ao programa de cadastro notas---".upper())
    print("""
    ------Opções------
    1 - Cadastrar notas
    2 - Mostrar média
    3 - Sair

    """)
    menu = input("Escolha entre 1 e 3: ")
    match menu:
        case "1":
            print("---Cadastrar Notas---".upper())
            n1 = float(input("Sua primeira nota: "))
            n2 = float(input("Sua segunda nota: "))
            n3 = float(input("Sua terceira nota: "))
            n4 = float(input("Sua quarta nota: "))
            print("---cadastro de notas feito com sucesso---".upper())
            print("-----------------------------")
            sleep(2)
        case "2":
            media = (n1 + n2 + n3 + n4)/4
            print("---mostrar média das notas---".upper())
            print(f"Sua média é: {media}")
            sleep(2)
        case "3":
            print("Saindo...")
            sleep(3)
            break
print("---Fora do sistema---".upper())
