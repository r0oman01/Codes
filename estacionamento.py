
placa_carro = input("Digite a placa: ")
hora_entrada = int(input("Digite a hora de entrada (0-23): "))
minuto_entrada = int(input("Digite os minutos de entrada (0-59): "))
hora_saida = int(input("Digite a hora de saída (0-23): "))
minuto_saida = int(input("Digite os minutos de saída (0-59): "))
valor_recibo = float()

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
        print("Hora adicional R$5,00")


    if total_minutos > 0:
        total += 5
        print("Hora adicional R$5,00")


lavagem = input("Vai fazer a lavagem? S ou N: ").upper()
if lavagem == 'S':
    total += 60
    print("A lavagem adiciona R$60,00")
print("-" * 20)


print(valor_recibo)

