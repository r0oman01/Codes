#variáveis
resto = int()
media = float()
x = int()

#processamento
num_1 = float(input("Digite um valor: "))
num_2 = float(input("Digite um valor: "))

resto_1 = num_1%2
resto_2 = num_2%2

media = (num_1 + num_2) / 2


#repetição da condição
while (resto_1 == 1) and (resto_2 == 1):
    x = int(input("Digite um valor novamente: "))

    resto_x = x%2

    if (resto_x == 0) or (x == 0):
        print("----------")
        break
else:
    print("-----------")

