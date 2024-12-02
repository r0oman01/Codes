from datetime import time
from time import sleep

print("sistema de cadastro de pessoas e notas".upper())
n1: float = 0
n2: float = 0
n3: float = 0
n4: float = 0
nome = str()
senha= str()

while True:
    print(f"cadastro de nome e senha".upper())
    print("""
        Opções
        1 - Cadastrar nome e senha
        2 - Entrar
        3 - Sair
        """)
    menu1 = input("Escolha entre 1 e 3: ")
    match menu1:
        case "1":
            nome = input("Digite seu nome para cadastro: ")
            senha = input("Digite sua senha para cadastro: ")
        case "2":
            verificacao_nome = input("Digite seu nome: ")
            verificacao_senha = input("Digite a sua senha: ")

            if verificacao_nome == nome and verificacao_senha == senha:
                while True:
                    print("programa de cadastro de notas".upper())
                    print("""
                    Opções
                    1 - Cadastrar notas
                    2 - Mostrar média
                    3 - Sair
        
                    """)

                    menu2 = input("Escolha entre 1 e 3: ")
                    match menu2:
                        case "1":
                            print("cadastro de notas".upper())
                            n1 = float(input("Sua primeira nota: "))
                            n2 = float(input("Sua segunda nota: "))
                            n3 = float(input("Sua terceira nota: "))
                            n4 = float(input("Sua quarta nota: "))
                            print("cadastro de notas feito com sucesso".upper())
                            sleep(2)
                        case "2":
                            media = (n1 + n2 + n3 + n4) / 4
                            print(f"Sua média é: {media}")
                            sleep(2)
                        case "3":
                            print("saindo...".upper())
                            sleep(3)
                            break
        case "3":
            print("saindo...".upper())
            sleep(3)
            break
print("fora do sistema".upper())
