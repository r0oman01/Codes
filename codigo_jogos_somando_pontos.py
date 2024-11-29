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
def registro_de_placar():
    if placarA > placarB and placarA > placarC and placarA > placarD:
        print(f"O {timeA} ganhou!")
    elif placarB > placarA and placarB > placarC and placarB > placarD:
        print(f"O {timeB} ganhou!")
    elif placarC > placarA and placarC > placarB and placarC > placarD:
        print(f"O {timeC} ganhou!")
    elif placarD > placarA and placarD > placarB and placarD > placarB:
        print(f"O {timeD} ganhou!")
#primeiro jogo timaA x timeB
placarA = int(input(f"Digite o placar do {timeA}: "))
placarB = int(input(f"Digite o placar do {timeB}: "))
if placarA > placarB:
    placar_definido_a += 3
    print(f"{placar_definido_a} pontos")
    print(f"O time {timeA} ganhou!")
elif placarB > placarA:
    placar_definido_b += 3
    print(f"{placar_definido_b} pontos")
    print(f"O time {timeB} ganhou!")
elif placarA == placarB:
    placar_definido_a += 1
    placar_definido_b += 1
    print("Empate!")
print("------")
#segundo jogo timeA x timeC
placarC = int(input(f"Digite o placar do {timeC}: "))
placarA = int(input(f"Digite o placar do {timeA}: "))
if placarC > placarA:
    placar_definido_c += 3
    print(f"{placar_definido_c} pontos")
    print(f"O time {timeC} ganhou!")
elif placarA > placarC:
    placar_definido_a += 3
    print(f"{placar_definido_a} pontos")
    print(f"O time {timeA} ganhou!")
elif placarA == placarC:
    placar_definido_c += 1
    placar_definido_a += 1
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
print("------")
print(f"Os pontos do {timeA}: {placar_definido_a}")
print(f"Os pontos do {timeB}: {placar_definido_b}")
print(f"Os pontos do {timeC}: {placar_definido_c}")
print(f"Os pontos do {timeD}: {placar_definido_d}")

maximo = max(placar_definido_a, placar_definido_b, placar_definido_c, placar_definido_d)

if placar_definido_a > placar_definido_b and placar_definido_a > placar_definido_c and placar_definido_a > placar_definido_d:
    print(f"O time {timeA} ganhou!!")
elif placar_definido_b > placar_definido_a and placar_definido_b > placar_definido_c and placar_definido_b > placar_definido_d:
    print(f"O time {timeB} ganhou!!")
elif placar_definido_c > placar_definido_a and placar_definido_c > placar_definido_b and placar_definido_c > placar_definido_d:
    print(f"O time {timeC} ganhou!!")
elif placar_definido_d > placar_definido_a and placar_definido_d > placar_definido_c and placar_definido_d > placar_definido_b:
    print(f"O time {timeD} ganhou!!")

if placar_definido_a == placar_definido_b or placar_definido_a == placar_definido_c or placar_definido_a == placar_definido_d:
    registro_de_placar()
elif placar_definido_b == placar_definido_a or placar_definido_b == placar_definido_c or placar_definido_b == placar_definido_d:
    registro_de_placar()
elif placar_definido_c == placar_definido_a or placar_definido_c == placar_definido_b or placar_definido_c == placar_definido_d:
    registro_de_placar()
elif placar_definido_d == placar_definido_a or placar_definido_d == placar_definido_c or placar_definido_d == placar_definido_b:
    registro_de_placar()
