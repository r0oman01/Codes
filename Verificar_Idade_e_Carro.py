import datetime as dt
ano = dt.datetime.now().year

nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano - ano_nascimento

if idade >= 18:
    carro = str(input("Escolha um carro entre Ferrari e Fusca: ")).capitalize()
    print(f"{nome.capitalize()} pode dirigir! Sua idade é: {idade}")
    match carro:
        case "Ferrari":
            print("Você pode ir até 290Km/h com este carro!")
        case "Fusca":
            print("Você pode ir até 140Km/h com este carro!")

else:
    print(f"{nome.capitalize()} não pode dirigir! Sua idade é: {idade}")

