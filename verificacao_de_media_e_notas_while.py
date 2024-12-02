from datetime import time
from time import sleep

print("---Sistema de cadastro de pessoas---".upper())
n1: float = 0
n2: float = 0
n3: float = 0
n4: float = 0
nome = str()
senha = str()

while True:
    print(f"Cadastro de nome e senha".upper())
    print("""
        ------Opções------
        1 - Cadastrar nome e senha
        2 - Entrar
        """)
    menu1 = input("Escolha entre 1 e 2: ")
    match menu1:
        case "1":
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
        case "2":
            verificacao_nome = input()
            verificacao_senha = input()
            if verificacao_nome == {nome} and verificacao_senha == {senha}:
                print("---sejam bem-vindos ao programa de cadastro notas---".upper())
                print("""
                    ------Opções------
                    1 - Cadastrar notas
                    2 - Mostrar média
                    3 - Sair
    
                    """)
                menu2 = input("Escolha entre 1 e 3: ")
                match menu2:
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
                        media = (n1 + n2 + n3 + n4) / 4
                        print("---mostrar média das notas---".upper())
                        print(f"Sua média é: {media}")
                        sleep(2)
                    case "3":
                        print("Saindo...")
                        sleep(3)
                        break
print("---Fora do sistema---".upper())

