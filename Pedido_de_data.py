#variáveis:

#processamento:
dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

#função para mostrar a data:
def mostrar_data():
    print("A data é: ", dia, "/", mes, "/", ano)


#função para verificar mês e dia:
def verificacao_mes_dia():
    if (mes > 12) or (dia > 31):
        print("Dados incorretos.")

    elif (mes > 12) and (dia > 31):
        print("Dados incorreto.")
    else:
        mostrar_data()  

#condição para verificar o mes e data:
if verificacao_mes_dia() == True:
    print(verificacao_mes_dia())

