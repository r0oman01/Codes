#variáveis

#processamento
print("Digite apenas F ou M!")
x = str(input("Digite o seu sexo: "))


#repetição
while(x != "M") and (x != "F"):
    y = str(input("Digite novamento o sexo: "))
    
    #caso y for igual M ou F
    if (y == "F") or (y == "M"):
        print("Válido!")
        break
else:
    print("Válido!")