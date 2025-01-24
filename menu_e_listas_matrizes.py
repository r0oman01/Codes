nomec = ""
idade = ""
usuarios = {}  # Para armazenar os usuários e suas bibliotecas

while True:
    print("""
    Opções:
    1 - Cadastro
    2 - Mostrar cadastros
    3 - Sair
    """)
    menu1 = input("Escolha a opção: ")

    match menu1:
        case "1":
            nomec = input("Digite seu nome: ")
            idade = input("Digite sua idade: ")
            usuarios[nomec] = {"idade": idade, "biblioteca": []}  # Criar um dicionário para o usuário
            print("Cadastro realizado com sucesso!")

        case "2":
            busca = input("Digite o nome ou idade para buscar: ").lower()
            encontrados = []
            for nome, dados in usuarios.items():
                if busca in nome.lower() or busca in dados["idade"]:
                    encontrados.append(nome)
            if encontrados:
                print("Pessoa(s) encontrada(s):")
                for i, nome in enumerate(encontrados, 1):
                    print(f"{i} - {nome} - Idade: {usuarios[nome]['idade']}")
            else:
                print("Nenhuma pessoa encontrada.")

        case "3":
            print("Saindo do sistema.")
            break
