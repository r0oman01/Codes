#variaveis times
timeA = (input("Digite o time A: "))
timeB = (input("Digite o time B: "))
timeC = (input("Digite o time C: "))
timeD = (input("Digite o time D: "))

placar_definido_a = 3
placar_definido_b = 3
placar_definido_c = 3
placar_definido_d = 3
print("------")

#processamento

#primeiro jogo timaA x timeB
placarA = int(input(f"Digite o placar do {timeA}: "))
placarB = int(input(f"Digite o placar do {timeB}: "))
if placarA > placarB:
    placarA = 3
    placarB = 0
    print(f"{placarA} pontos")
    print(f"O time {timeA} ganhou!")
elif placarB > placarA:
    placarB = 3
    placarA = 0
    print(f"{placarB} pontos")
    print(f"O time {timeB} ganhou!")
elif placarA == placarB:
    placar_definido_a += 1
    placar_definido_b += 1
    print("Empate!")

print("------")

#segundo jogo timeA x timeC
placarC = int(input(f"Digite o placar do {timeC}: "))
placarD = int(input(f"Digite o placar do {timeD}: "))
if placarC > placarD:
    placarC = 3
    placarD = 0
    print(f"{placarC} pontos")
    print(f"O time {timeC} ganhou!")
elif placarD > placarC:
    placarD = 3
    placarC = 0
    print(f"{placarD} pontos")
    print(f"O time {timeD} ganhou!")
elif placarD == placarC:
    placar_definido_c += 1
    placar_definido_d += 1
    print("Empate!")

print("------")

#terceiro jogo timeA x timeD
placarA = int(input(f"Digite o placar do {timeA}: "))
placarD = int(input(f"Digite o placar do {timeD}: "))
if placarA > placarD:
    placar_definido_a += 3
    print(f"{placar_definido_a} pontos")
    print(f"O time {timeA} ganhou!")
elif placarD > placarA:
    placar_definido_d += 3
    print(f"{placar_definido_d} pontos")
    print(f"O time {timeD} ganhou!")
elif placarD == placarA:
    placar_definido_d += 1
    placar_definido_a += 1
    print("Empate!")

print("------")

#quarto jogo timeB x timeC
placarB = int(input(f"Digite o placar do {timeB}: "))
placarC = int(input(f"Digite o placar do {timeC}: "))
if placarB > placarC:
    placar_definido_b += 3
    print(f"{placar_definido_b} pontos")
    print(f"O time {timeB} ganhou!")
elif placarC > placarB:
    placar_definido_c += 3
    print(f"{placar_definido_c} pontos")
    print(f"O time {timeC} ganhou!")
elif placarB == placarC:
    placar_definido_b += 1
    placar_definido_c += 1
    print("Empate!")

print("------")

#quinto jogo timeB x timeD
placarB = int(input(f"Digite o placar do {timeB}: "))
placarD = int(input(f"Digite o placar do {timeD}: "))
if placarB > placarD:
    placar_definido_b += 3
    print(f"{placar_definido_b} pontos")
    print(f"O time {timeB} ganhou!")
elif placarD > placarB:
    placar_definido_d += 3
    print(f"{placar_definido_d} pontos")
    print(f"O time {timeD} ganhou!")
elif placarD == placarB:
    placar_definido_b += 1
    placar_definido_d += 1
    print("Empate!")

print("------")

#sexto jogo timeC x timeD
placarC = int(input(f"Digite o placar do {timeC}: "))
placarD = int(input(f"Digite o placar do {timeD}: "))
if placarC > placarD:
    placar_definido_c += 3
    print(f"{placar_definido_c} pontos")
    print(f"O time {timeC} ganhou!")
elif placarD > placarC:
    placar_definido_d += 3
    print(f"{placar_definido_d} pontos")
    print(f"O time {timeD} ganhou!")
elif placarD == placarC:
    placar_definido_c += 1
    placar_definido_d += 1
    print("Empate!")








