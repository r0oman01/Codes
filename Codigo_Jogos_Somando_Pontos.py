#variaveis times
timeA = (input("Digite o time A: "))
timeB = (input("Digite o time B: "))
timeC = (input("Digite o time C: "))
timeD = (input("Digite o time D: "))
print("------")

placar_definido_a = 0
placar_definido_b = 0
placar_definido_c = 0
placar_definido_d = 0
#processamento

#primeiro jogo timaA x timeB
placarA = int(input(f"Digite o placar do {timeA.capitalize()}: "))
placarB = int(input(f"Digite o placar do {timeB.capitalize()}: "))
if placarA > placarB:
    placar_definido_a += 3
    print(f"{placar_definido_a} pontos")
    print(f"O time {timeA.capitalize()} ganhou!")
elif placarB > placarA:
    placar_definido_b += 3
    print(f"{placar_definido_b} pontos")
    print(f"O time {timeB.capitalize()} ganhou!")
elif placarA == placarB:
    placar_definido_a += 1
    placar_definido_b += 1
    print("Empate!")
print("------")
#segundo jogo timeA x timeC
placarC = int(input(f"Digite o placar do {timeC.capitalize()}: "))
placarA = int(input(f"Digite o placar do {timeA.capitalize()}: "))
if placarC > placarA:
    placar_definido_c += 3
    print(f"{placar_definido_c} pontos")
    print(f"O time {timeC.capitalize()} ganhou!")
elif placarA > placarC:
    placar_definido_a += 3
    print(f"{placar_definido_a} pontos")
    print(f"O time {timeA.capitalize()} ganhou!")
elif placarA == placarC:
    placar_definido_c += 1
    placar_definido_a += 1
    print("Empate!")
print("------")
#terceiro jogo timeA x timeD
placarA = int(input(f"Digite o placar do {timeA.capitalize()}: "))
placarD = int(input(f"Digite o placar do {timeD.capitalize()}: "))
if placarA > placarD:
    placar_definido_a += 3
    print(f"{placar_definido_a} pontos")
    print(f"O time {timeA.capitalize()} ganhou!")
elif placarD > placarA:
    placar_definido_d += 3
    print(f"{placar_definido_d} pontos")
    print(f"O time {timeD.capitalize()} ganhou!")
elif placarD == placarA:
    placar_definido_d += 1
    placar_definido_a += 1
    print("Empate!")
print("------")
#quarto jogo timeB x timeC
placarB = int(input(f"Digite o placar do {timeB.capitalize()}: "))
placarC = int(input(f"Digite o placar do {timeC.capitalize()}: "))
if placarB > placarC:
    placar_definido_b += 3
    print(f"{placar_definido_b} pontos")
    print(f"O time {timeB.capitalize()} ganhou!")
elif placarC > placarB:
    placar_definido_c += 3
    print(f"{placar_definido_c} pontos")
    print(f"O time {timeC.capitalize()} ganhou!")
elif placarB == placarC:
    placar_definido_b += 1
    placar_definido_c += 1
    print("Empate!")
print("------")
#quinto jogo timeB x timeD
placarB = int(input(f"Digite o placar do {timeB.capitalize()}: "))
placarD = int(input(f"Digite o placar do {timeD.capitalize()}: "))
if placarB > placarD:
    placar_definido_b += 3
    print(f"{placar_definido_b} pontos")
    print(f"O time {timeB.capitalize()} ganhou!")
elif placarD > placarB:
    placar_definido_d += 3
    print(f"{placar_definido_d} pontos")
    print(f"O time {timeD.capitalize()} ganhou!")
elif placarD == placarB:
    placar_definido_b += 1
    placar_definido_d += 1
    print("Empate!")
print("------")
#sexto jogo timeC x timeD
placarC = int(input(f"Digite o placar do {timeC.capitalize()}: "))
placarD = int(input(f"Digite o placar do {timeD.capitalize()}: "))
if placarC > placarD:
    placar_definido_c += 3
    print(f"{placar_definido_c} pontos")
    print(f"O time {timeC.capitalize()} ganhou!")
elif placarD > placarC:
    placar_definido_d += 3
    print(f"{placar_definido_d} pontos")
    print(f"O time {timeD.capitalize()} ganhou!")
elif placarD == placarC:
    placar_definido_c += 1
    placar_definido_d += 1
    print("Empate!")
print("------")
print(f"Os pontos do {timeA.capitalize()}: {placar_definido_a}")
print(f"Os pontos do {timeB.capitalize()}: {placar_definido_b}")
print(f"Os pontos do {timeC.capitalize()}: {placar_definido_c}")
print(f"Os pontos do {timeD.capitalize()}: {placar_definido_d}")


if placar_definido_a > placar_definido_b and placar_definido_a > placar_definido_c and placar_definido_a > placar_definido_d:
    print(f"O time {timeA.capitalize()} ganhou!!")
elif placar_definido_a == placar_definido_b or placar_definido_a == placar_definido_c or placar_definido_a == placar_definido_d:
    if placarA > placarB and placarA > placarC and placarA > placarD:
        print(f"O {timeA.capitalize()} ganhou!")

if placar_definido_b > placar_definido_a and placar_definido_b > placar_definido_c and placar_definido_b > placar_definido_d:
    print(f"O time {timeB.capitalize()} ganhou!!")
elif placar_definido_b == placar_definido_a or placar_definido_b == placar_definido_c or placar_definido_b == placar_definido_d:
    if placarB > placarA and placarB > placarC and placarB > placarD:
        print(f"O {timeB.capitalize()} ganhou!")

if placar_definido_c > placar_definido_a and placar_definido_c > placar_definido_b and placar_definido_c > placar_definido_d:
    print(f"O time {timeC.capitalize()} ganhou!!")
elif placar_definido_c == placar_definido_a or placar_definido_c == placar_definido_b or placar_definido_c == placar_definido_d:
    if placarC > placarA and placarC > placarB and placarC > placarD:
        print(f"O {timeC.capitalize()} ganhou!")

if placar_definido_d > placar_definido_a and placar_definido_d > placar_definido_c and placar_definido_d > placar_definido_b:
    print(f"O time {timeD.capitalize()} ganhou!!")
elif placar_definido_d == placar_definido_a or placar_definido_d == placar_definido_c or placar_definido_d == placar_definido_b:
    if placarD > placarA and placarD > placarB and placarD > placarC:
        print(f"O {timeD.capitalize()} ganhou!")





