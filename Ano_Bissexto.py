#variáveis


#processamento

#função para verificar o resto:
def vericacao_resto():
    if calculo == 0:
        print("Ano bissexto!")

    elif calculo == 1:
        print("Ano não bissexto!")

#inserir um valor:
ano = int(input("Digite um ano: "))

#cálculo para saber o resto:
calculo = ano%4
print(calculo)

#verificando se a função é verdadeira:
if vericacao_resto() == True:
    print(vericacao_resto())