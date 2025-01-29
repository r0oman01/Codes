import flet as ft

def main(page:ft.Page):
    page.title = "Soma de valores"
    def calc(e):
        texto_resposta.value = float(v1.value) + float(v2.value) # atribuindo soma dos valroes em "texto_resposta"
        texto_resposta.update()

    v1 = ft.TextField(label="Digite seu valor: ")
    v2 = ft.TextField(label="Digite seu valor: ")
    btnCalcular = ft.ElevatedButton(text = "Calcular", on_click=calc)
    texto_resposta = ft.Text("Aqui vai aparecer a resposta")
    page.add(v1, v2, btnCalcular, texto_resposta)



    page.update()

if __name__ == "__main__":
    ft.app(main)