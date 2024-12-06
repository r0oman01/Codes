armazenar_placas = []
valores_armazenados = []
while True:
    placa_carro = input("Digite a placa: ")
    hora_entrada = int(input("Digite a hora de entrada (0-23): "))
    minuto_entrada = int(input("Digite os minutos de entrada (0-59): "))
    hora_saida = int(input("Digite a hora de saída (0-23): "))
    minuto_saida = int(input("Digite os minutos de saída (0-59): "))

    minutos_entrada = hora_entrada * 60 + minuto_entrada
    minutos_saida = hora_saida * 60 + minuto_saida
    total_minutos = minutos_saida - minutos_entrada


    print(f"Total de minutos: {total_minutos} minutos.")

    if total_minutos <= 60:
        total = 15
        print("Até 60 minutos, valor a pagar é de: R$15,00")
    else:

        total_minutos -= 60
        total = 15
        print(f"Valor padrão: R$15,00")


        while total_minutos >= 60:
            total_minutos -= 60
            total += 5
            print("Hora adicional: R$5,00")


        if total_minutos > 0:
            total += 5
            print("Hora adicional: R$5,00")


    lavagem = input("Vai fazer a lavagem? S ou N: ").upper()
    if lavagem != 'N':
        total += 60
        print("A lavagem adiciona R$60,00")
        print("-" * 20)
        print(f"Valor total a pagar: R$ {total:.2f}")
        print("-" * 20)
    armazenar_placas.append(placa_carro)
    valores_armazenados.append(total)
    cadastrar_carro = str(input("Quer cadastrar outro carro?")).upper()
    if cadastrar_carro == "N":
        break
print("As placa dos carros registrados são:")
for x in range(len(armazenar_placas)):
    print(armazenar_placas[x], f"O total a ser pago é: {valores_armazenados[x]}")
