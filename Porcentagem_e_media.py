#variáveis
hora_total = 120


#procassamento
nota_1 = float(input("Valor nota 1:"))
nota_2 = float(input("Valor nota 2:"))
nota_3 = float(input("Valor nota 3:"))
faltas = int(input("Quantas faltas: "))

media = (nota_1 + nota_2 + nota_3) / 3

porcentagem = faltas*4/hora_total*100

#fazer a verificação da media e porcentagem
def verificar_media_e_porcentagem():
    if (media >= 7) and (media <= 10) and (porcentagem <= 25):
        print("Parabéns, você foi aprovado! A sua média é", media, "e a sua porcentagem é", porcentagem, "%")

    elif (media <= 6) and (media >= 0) and (porcentagem<= 25):
        print("Você está de recuperação! A sua média é", media, "e a sua porcentagem é",porcentagem, "%")

    elif (media < 6) or (porcentagem > 25):
        print("Você está reprovado! A sua média é", media, "e a sua porcentagem é", porcentagem, "%")

if verificar_media_e_porcentagem() == True:
    print(verificar_media_e_porcentagem())