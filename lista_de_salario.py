# nomes = ["gabriel", "fernando", "rogério", "roman", "pedro", "juliana", "barbara"]
# novos_nomes = ["denys", "felipe", "joao", "vitor", "ana", "julia", "margarida", "claudio"]
#
# nomes.sort()
# print(nomes)
# nomes.append(novos_nomes)
# print(nomes)
#
# nomes2 = nomes.copy()
# nomes2.remove("barbara")
# print(nomes2)
#
# print(nomes[1:7])

sal = [1200, 1300, 4000, 900, 20000,3000]
listaNova = []
for valor in sal:
    listaNova.append(valor * 1.05)
print(sal)
print(listaNova)
print(sum(listaNova))

media = sum(listaNova)/len(sal)
print(media)