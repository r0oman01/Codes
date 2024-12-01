#variaveis
timeA = input("Digite o time A: ")
timeB = input("Digite o time B: ")
timeC = input("Digite o time C: ")
timeD = input("Digite o time D: ")
ganhador1 = str()
ganhador2 = str()

print("----------")
#processo
#verificacao do placar
print("Semifinal")
print("----------")
print(f"Primeiro jogo: {timeA.upper()} X {timeB.upper()} ")
placarA = input(f"Digite a pontuação do {timeA.upper()}: ")
placarB = input(f"Digite a pontuação do {timeB.upper()}: ")

if placarA > placarB:
    print(f"O time {timeA.upper()} ganhou!")
    ganhador1 = timeA
elif placarB > placarA:
    print(f"O time {timeB.upper()} ganhou!")
    ganhador1 = timeB
elif placarA == placarB:
    ganhador1 = "Empate"
    print("Empate!")
    placar_empate_A = input(f"Pontuação dos pênaltis do time {timeA.upper()}: ")
    placar_empate_B = input(f"Pontuação dos pênaltis do time {timeB.upper()}: ")

    if placar_empate_A > placar_empate_B:
        print(f"O time {timeA.upper()} venceu!")
        ganhador1 = timeA
    elif placar_empate_B > placar_empate_A:
        print(f"O time {timeB.upper()} venceu!")
        ganhador1 = timeB
    else:
        print("Valores inválidos!")

print("----------")
print(f"Segundo jogo: {timeC.upper()} X {timeD.upper()} ")
placarC = input(f"Digite a pontuação do {timeC.upper()}: ")
placarD = input(f"Digite a pontuação do {timeD.upper()}: ")

if placarC > placarD:
    print(f"O time {timeC.upper()} ganhou!")
    ganhador2 = timeC
elif placarD > placarC:
    print(f"O time {timeD.upper()} ganhou!")
    ganhador2 = timeD
elif placarC == placarD:
    ganhador2 = "Empate"
    print("Empate!")
    placar_empate_C = input(f"Pontuação dos pênaltis {timeC.upper()}: ")
    placar_empate_D = input(f"Pontuação dos pênaltis {timeD.upper()}: ")

    if placar_empate_C > placar_empate_D:
        print(f"O time {timeC.upper()} venceu!")
        ganhador2 = timeC
    elif placar_empate_D > placar_empate_C:
        print(f"O time {timeD.upper()} venceu!")
        ganhador2 = timeD
    else:
        print("Valores inválidos!")


print("----------")
print("Jogo Final")
print(f"Último jogo: {ganhador1.upper()} X {ganhador2.upper()}")

placar_ganhador_1 = input(f"Digite a pontuação do time {ganhador1.upper()}: ")
placar_ganhador_2 = input(f"Digite a pontuação do time {ganhador2.upper()}: ")

if placar_ganhador_1 > placar_ganhador_2:
    print(f"Time {ganhador1.upper()} venceu!")
elif placar_ganhador_2 > placar_ganhador_1:
    print(f"Time {ganhador2.upper()} venceu!")
elif placar_ganhador_1 == placar_ganhador_2:
    print("Empate!")
    placar_ganhador_empate_1 = input(f"Pontuação dos pênaltis do time {ganhador1.upper()}: ")
    placar_ganhador_empate_2 = input(f"Pontuação dos pênaltis do time {ganhador2.upper()}: ")
    if placar_ganhador_empate_1 > placar_ganhador_empate_2:
        print(f"O ganhador foi {ganhador1.upper()}!")
    else:
        print(f"O ganhador foi {ganhador2.upper()}!")



















