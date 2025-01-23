# clientes = []
#
# cliente = ("Gabriel", "000-000-000-00")
# clientes.append(cliente)
# print(clientes)
#
# cliente = ("Rodrigo", "000-000-000-00")
# clientes.append(cliente)
# print(clientes)
#
# clientes[0][0] = "Ricardo"
# print(clientes[0])

# capitais = {
#     ("Brasil", "São Paulo"): "São Paulo",
#     ("Brasil", "Minas Gerais"): "Belo Horizonte",
#     ("Brasil", "Rio de Janeiro"): "Rio de Janeiro"
# }
# print(capitais.keys())
# print(capitais.values())

# tupla = (1,2,3,3,3,4,5,6)
# print(tupla.count(3))
# print(tupla.index(3))

lista_materiais =[]
def CadastroMateriais(nome, codigo, unidade, quantidade):
    tupla = (nome, codigo, unidade, quantidade)
    lista_materiais.append(tupla)
    return lista_materiais

def ConsultarMaterial(codigo):
    for material in lista_materiais:
        if material[1] == codigo:
            return print(material)
        else:
            pass

CadastroMateriais("Cimento", "1", 12, 24)
CadastroMateriais("Papel", "2", 1, 3)
print(lista_materiais)

ConsultarMaterial(1)
