import flet as ft

# Lista de personagens
personagens = []


def main(page: ft.Page):
    # Função para atualizar a lista de personagens na interface
    def atualizar_lista():
        lista_personagens.controls.clear()
        for personagem in personagens:
            lista_personagens.controls.append(
                ft.Column(
                    controls=[
                        ft.Text(f"Nome: {personagem['nome']}", size=16, weight="bold"),
                        ft.Text(f"Idade: {personagem['idade']}"),
                        ft.Text(f"Classe: {personagem['classe']}"),
                        ft.Text(f"Habilidade: {personagem['habilidade']}"),
                        ft.Divider()
                    ],
                    alignment=ft.MainAxisAlignment.START
                )
            )
        page.update()

    # Função para adicionar um novo personagem
    def adicionar_personagem():
        nome = campo_nome.value.strip()
        idade = campo_idade.value.strip()
        classe = campo_classe.value.strip()
        habilidade = campo_habilidade.value.strip()

        if nome and idade and classe and habilidade:
            personagens.append({
                'nome': nome,
                'idade': idade,
                'classe': classe,
                'habilidade': habilidade
            })
            # Limpar campos de entrada
            campo_nome.value = ""
            campo_idade.value = ""
            campo_classe.value = ""
            campo_habilidade.value = ""
            page.update()
            atualizar_lista()
        else:
            page.add(ft.Text("Por favor, preencha todos os campos!", color=ft.colors.RED))

    # Componentes da interface
    campo_nome = ft.TextField(label="Nome do Personagem")
    campo_idade = ft.TextField(label="Idade do Personagem")
    campo_classe = ft.TextField(label="Classe do Personagem")
    campo_habilidade = ft.TextField(label="Habilidade do Personagem")

    botao_adicionar = ft.ElevatedButton("Adicionar Personagem", on_click=lambda e: adicionar_personagem())

    lista_personagens = ft.Column()

    # Organizando a página
    page.add(
        campo_nome,
        campo_idade,
        campo_classe,
        campo_habilidade,
        botao_adicionar,
        ft.Divider(),
        lista_personagens
    )


# Inicializando o aplicativo Flet
ft.app(target=main)
