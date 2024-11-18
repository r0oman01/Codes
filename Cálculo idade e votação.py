#variáveis
atual = int(2024)
idade = int()



#Processamento

#definir funções

#funcção para verficação de parentesco
def verificacao_de_pais():
    if (pais == "SIM") or (pais == "sim"):
        print("Você mora com os pais!")

    elif (pais == "NÃO") or (pais == "não"):
        print("Você não mora com os pais!")

#função de verificação de salário:
def veficacao_beneficio_salario():
    if (sal > 10000):
        print("Seu salário é: R$", sal)
        print("Você não está de acordo com os termos para os benefícios.")

    elif (sal >= 1000) and (sal < 5000) or (sal < 1000):
         print("Seu salário é: R$", sal)
         print("Você está apto a receber os benefícios.") 
  

#função verificação votação:
def verificacao_de_idade():
    if idade < 16:
        print("Você não pode votar!")

    elif (idade >= 16) and (idade < 18) or (idade > 70):
        print("Seu voto é facultativo!")
        
    elif (idade >= 18) and (idade < 70):
        print("Seu voto é obrigatório!")

#leitura do tipo de variável
def verificacao_de_tipo():
    print(type(nasc))




#pergunta parental
pais = str(input("Mora com os pais? Apenas responda SIM ou NÃO: "))

#ano de nascimento
nasc = int(input("Seu ano de nascimento:"))


#salário
sal = float(input("Digite o seu salário:"))


#idade !
idade = atual - nasc  
print("Sua idade é:", idade)


#mostrar tipo tipo:
print(verificacao_de_tipo())

"""
#verificação de tipo:
if type(nasc) != str(nasc):
    print("Dados incorretos!")
"""

#veficação de parentesco
if verificacao_de_pais() == True:
    print(verificacao_de_pais())

elif verificacao_de_idade() == True:
    print(verificacao_de_idade())

elif veficacao_beneficio_salario() == True:
    print(veficacao_beneficio_salario())

