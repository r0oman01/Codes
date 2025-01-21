import math
# #list - lista
# nomes = ["carlos", "pedro", "gabriel"]
# idades = list()
#
# nomes.append("zé")
# print(nomes)
#
# #append
# idades.append(90000000000)
# idades.append(10239434)
# idades.append(60)
# idades.append(10)
# idades.append(6)
# print(idades)
#
# # #remove e pop
# # nomes.pop(1)
# # print(nomes)
# # nomes.remove("carlos")
#
#
# #copy
# valores = idades.copy()
# valores.append(30)
# print(valores)
#
# #sort
# valores.sort()
# print(valores)
# valores.reverse()
# print(valores)
#
# print(nomes.count("pedro"))
#
# #index
# print(nomes[0:5])

valores = [2,4,3,5,6,7,6,5,3.4,3,10,100.43,5]
print(sum(valores))
print(len(valores))
print("-"*20)
#iteracao de lista
listaNova = []
for valor in valores:
    listaNova.append(valor+2)
print(valores)
print(listaNova)
