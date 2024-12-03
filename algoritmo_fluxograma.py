from datetime import time
from time import sleep

print("sistema de cadastro de pessoas e produtos".upper())
produto = str()
valor = float()
nome = str()
senha = str()

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
            sleep(2)
        case "2":
            print("para entrar no sistema de cadastro de produto, é necessário fazer o seu login".upper())
            verificacao_nome = input("Digite seu nome: ")
            verificacao_senha = input("Digite a sua senha: ")
            sleep(2)

            if verificacao_nome == nome and verificacao_senha == senha:
                sleep(2)
                while True:
                    print("programa de cadastro de produto e valor".upper())
                    print("""
Opções
1 - Cadastrar produto e valor
2 - Mostrar produto e valor
3 - Sair

                    """)

                    menu2 = input("Escolha entre 1 e 3: ")
                    match menu2:
                        case "1":
                            print("cadastro de produto e valor".upper())
                            produto = str(input("Digite o nome do seu produto: "))
                            valor = float(input("Digite o valor do seu produto: "))
                            sleep(2)
                            print("cadastro de produto e valor feito com sucesso".upper())
                            sleep(2)
                        case "2":
                            print(f"Seu produto é: {produto.capitalize()}")
                            print(f"Seu valor é: R${valor}")
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