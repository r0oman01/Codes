cont = int()
soma = int()
for cont in range(1,501):
    if cont % 2 == 1 and cont % 3 == 0:
        print(cont)
        soma = soma + cont
print(soma)