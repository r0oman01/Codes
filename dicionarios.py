# cadastro1 = {"nome": "carlos", "senha":123, "cpf": "11111111111"}
# cadastro2 = {"nome": "renata", "senha":123, "cpf": "22222222222"}
# cadastro3 = {"nome": "gabriel", "senha":123, "cpf": "33333333333"}
#
#
# cadastros = [cadastro1, cadastro2, cadastro3]
#
# # nome = input("Digite seu nome: ")
# # senha = int(input("Digite a sua senha: "))
# #
# # for c in cadastros:
# #     if nome == c["nome"] and senha == c["senha"]:
# #         print("Entrou no sistema!")
# #     else:
# #         print("Dados inválidos!")
# #         break
#
# #mudar valores
# cadastro1["nome"] = "roberto"
# print(cadastro1["nome"])
#
# #adicionar valores e chaves
# cadastro1["salario"] = 1200
# print(cadastro1["salario"])
#
# #pegar apenas os valores
# print(cadastro1.values())
# #pegar apenas as chaves
# print(cadastro1.keys())
# #pega tudo
# print(cadastro1.items())
#
# # for c in cadastro1.items():
# #     print(c)
# #
# # for k,v in cadastro1.items():
# #     print(k)
#


produto = {"nome":"","marca":"", "valor": ""}
list_produto = list()
while True:
    nome_produto = input("Digite o nome do produto: ")
    marca_produto = input("Digite a marca do produto: ")
    valor_produto = input("Digite o valor do produto: ")

    produto["nome"] = nome_produto
    produto["marca"] = marca_produto
    produto["valor"] = valor_produto
    print(produto.values())
    print(list_produto.append(produto))





