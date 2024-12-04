import datetime as dt
from datetime import datetime, timedelta
from time import sleep
print("Tabela de produtos!".upper())
nome = str(input("Digite seu nome: "))
tel = int(input("Digite seu telefone: "))
idade = int(input("Digite sua idade: "))
produto = str()
valor = float()
data = datetime.now().date()


print(f"""
Seus dados:
Nome: {nome.capitalize()}
Tel.: {tel}
Idade: {idade}
    """)
while True:
    print("""
1 - Cadastrar produto
2 - Sair
    """)
    menu1 = int(input("Escolha a sua opção entre 1 e 2: "))

    match menu1:
        case 1:
            print(f"""
Produtos a ser cadastrado:
1 produto: 1
2 produtos: 2
3 produtos: 3
4 produtos: 4
5 produtos: 5
6 - Sair
                """)
            menu2 = int(input("Escolha quantos produtos você quer cadastrar: "))
            match menu2:
                case 1:
                    produto = str(input("Nome do produto: "))
                    unitario1 = int(input("Quantidade de produtos: "))
                    valor = float(input("Valor do produto: "))
                    unitario_total = unitario1
                    print(f"""
Qntd.                  Produto     Valor
{unitario_total}       {produto}   {f"R$ {valor * unitario1}"}
-----------------------------------                         
Valor total: {f"R$ {(valor * unitario1)}"}
Data do recibo: {data}
""")
                case 2:
                    produto = str(input("Nome do produto: "))
                    unitario1 = int(input("Quantidade de produtos: "))
                    produto2 = str(input("Nome do produto: "))
                    unitario2 = int(input("Quantidade de produtos: "))
                    valor = float(input("Valor do produto: "))
                    valor2 = float(input("Valor do produto: "))
                    unitario_total = unitario1 + unitario2
                    print(f"""
Qntd.                  Produto             Valor
{unitario1}      {produto}           {f"R$ {valor * unitario1}"}
-------------------------------------------
{unitario2}      {produto2}          {f"R$ {valor2 * unitario2}"}
-------------------------------------------
Valor total: {f"R$ {(valor * unitario1) + (valor2 * unitario2)}"}
Data do recibo: {data}
""")
                case 3:
                    produto = str(input("Nome do produto: "))
                    unitario1 = int(input("Quantidade de produtos: "))
                    produto2 = str(input("Nome do produto: "))
                    unitario2 = int(input("Quantidade de produtos: "))
                    produto3 = str(input("Nome do produto: "))
                    unitario3 = int(input("Quantidade de produtos: "))
                    valor = float(input("Valor do produto: "))
                    valor2 = float(input("Valor do produto: "))
                    valor3 = float(input("Valor do produto: "))
                    unitario_total = unitario1 + unitario2 + unitario3
                    print(f"""
Qntd.                  Produto                  Valor
{unitario1}       {produto}              {f"R$ {valor * unitario1}"}
----------------------------------------------
{unitario2}        {produto2}             {f"R$ {valor2 * unitario2}"}
----------------------------------------------
{unitario3}        {produto3}             {f"R$ {valor3 * unitario3}"}
----------------------------------------------
Valor total: {f"R$ {(valor * unitario1) + (valor2 * unitario2) + (valor3 * unitario3)}"}
Data do recibo: {data}
""")
                case 4:
                    produto = str(input("Nome do produto: "))
                    unitario1 = int(input("Quantidade de produtos: "))
                    produto2 = str(input("Nome do produto: "))
                    unitario2 = int(input("Quantidade de produtos: "))
                    produto3 = str(input("Nome do produto: "))
                    unitario3 = int(input("Quantidade de produtos: "))
                    produto4 = str(input("Nome do produto: "))
                    unitario4 = int(input("Quantidade de produtos: "))
                    valor = float(input("Valor do produto: "))
                    valor2 = float(input("Valor do produto: "))
                    valor3 = float(input("Valor do produto: "))
                    valor4 = float(input("Valor do produto: "))
                    unitario_total = unitario1 + unitario2 + unitario3 + unitario4
                    print(f"""
Qntd.              Produto              Valor
{unitario1}       {produto}           {f"R$ {valor * unitario1}"}
----------------------------------------------
{unitario2}        {produto2}          {f"R$ {valor2 * unitario2}"}
----------------------------------------------
{unitario3}        {produto3}          {f"R$ {valor3 * unitario3}"}
----------------------------------------------
{unitario4}        {produto4}          {f"R$ {valor4 * unitario3}"}
----------------------------------------------

Valor total: {f"R$ {(valor * unitario1) + (valor2 * unitario2) + (valor3 * unitario3) + (valor4 * unitario4)}"}
Data do recibo: {data}
""")

                case 5:
                    produto = str(input("Nome do produto: "))
                    unitario1 = int(input("Quantidade de produtos: "))
                    produto2 = str(input("Nome do produto: "))
                    unitario2 = int(input("Quantidade de produtos: "))
                    produto3 = str(input("Nome do produto: "))
                    unitario3 = int(input("Quantidade de produtos: "))
                    produto4 = str(input("Nome do produto: "))
                    unitario4 = int(input("Quantidade de produtos: "))
                    produto5 = str(input("Nome do produto: "))
                    unitario5 = int(input("Quantidade de produtos: "))
                    valor = float(input("Valor do produto: "))
                    valor2 = float(input("Valor do produto: "))
                    valor3 = float(input("Valor do produto: "))
                    valor4 = float(input("Valor do produto: "))
                    valor5 = float(input("Valor do produto: "))
                    unitario_total = unitario1 + unitario2 + unitario3 + unitario4 + unitario5
                    print(f"""
Qntd.                  Produto              Valor
{unitario1}       {produto}           {f"R$ {valor * unitario1}"}
----------------------------------------------
{unitario2}       {produto2}          {f"R$ {valor2 * unitario2}"}
----------------------------------------------
{unitario3}       {produto3}          {f"R$ {valor3 * unitario3}"}
----------------------------------------------
{unitario4}        {produto4}          {f"R$ {valor4 * unitario4}"}
----------------------------------------------
{unitario5}        {produto5}          {f"R$ {valor5 * unitario5}"}
----------------------------------------------


Valor total: {f"R$ {(valor * unitario1) + (valor2 * unitario2) + (valor3 * unitario3) + (valor4 * unitario4) + (valor5 * unitario5)}"}
Data do recibo: {data}
""")

                case 6:
                    print("Saindo...")
                    sleep(3)
                    break


        case 2:
            print("Saindo...")
            sleep(3)
            break









