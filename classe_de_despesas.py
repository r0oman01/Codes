import flet as ft

class Usuario:
    def __init__(self, nome, idade, cor, genero, estado_civil, usuario, senha, renda_mensal=None):
        self._nome = nome
        self._idade = idade
        self._cor = cor
        self._genero = genero
        self._estado_civil = estado_civil
        self._usuario = usuario
        self._senha = senha
        self._renda_mensal = renda_mensal  # Novo atributo para renda mensal

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade >= 0:
            self._idade = idade
        else:
            print("Idade inválida!")

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def estado_civil(self):
        return self._estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil):
        self._estado_civil = estado_civil

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def renda_mensal(self):
        return self._renda_mensal

    @renda_mensal.setter
    def renda_mensal(self, renda):
        if renda is not None and renda >= 0:
            self._renda_mensal = renda
        else:
            print("Valor inválido para renda mensal!")

    def exibir_dados(self):
        dados = f"Nome: {self.nome}\nIdade: {self.idade}\nCor: {self.cor}\nGênero: {self.genero}\nEstado Civil: {self.estado_civil}\n"
        if self.renda_mensal is not None:
            dados += f"Renda Mensal: R${self.renda_mensal:.2f}"
        return dados


def tela_de_login(page: ft.Page, usuario: Usuario):
    # Criando os campos de login
    usuario_input = ft.TextField(label="Nome de usuário", autofocus=True)
    senha_input = ft.TextField(label="Senha", password=True)

    # Botão de login
    login_button = ft.ElevatedButton("Login", on_click=lambda e: fazer_login(page, usuario, usuario_input, senha_input))

    # Adiciona os campos e botão na tela
    page.add(usuario_input, senha_input, login_button)


def fazer_login(page: ft.Page, usuario: Usuario, usuario_input: ft.TextField, senha_input: ft.TextField):
    # Verificar se os dados de login estão corretos
    if usuario_input.value == usuario.usuario and senha_input.value == usuario.senha:
        # Limpa a tela e exibe os dados do usuário
        page.clean()
        page.add(ft.Text("Login bem-sucedido!"))
        page.add(ft.Text(usuario.exibir_dados()))

        # Mostrar dados de Despesas e Receitas (apenas para demonstração)
        exibir_despesas_receitas(page)
    else:
        # Caso o login seja falho
        page.clean()
        page.add(ft.Text("Usuário ou senha incorretos!"))


def exibir_despesas_receitas(page: ft.Page):
    # Classe Despesas
    class Despesas:
        def __init__(self, valor: float, descricao: str, realizado: bool = False):
            self.valor = valor
            self.descricao = descricao
            self.realizado = realizado

        def imprimir_despesa(self):
            status = "Realizado" if self.realizado else "Não realizado"
            return f"\nDespesa: {self.descricao}\nValor: R${self.valor:.2f}\nStatus: {status}"

    # Classe Receita
    class Receita:
        def __init__(self, valor: float, descricao: str, recebida: bool = False):
            self.valor = valor
            self.descricao = descricao
            self.recebida = recebida

        def imprimir_receita(self):
            status = "Recebida" if self.recebida else "Não recebida"
            return f"\nReceita: {self.descricao}\nValor: R${self.valor:.2f}\nStatus: {status}"

    # Criar instâncias de Despesas e Receita
    despesa = Despesas(200.00, "Pagamento de fatura")
    receita = Receita(1000.00, "Recebimento de pagamento de cliente")

    # Exibir despesa e receita na tela
    page.add(ft.Text(despesa.imprimir_despesa()))
    page.add(ft.Text(receita.imprimir_receita()))


# Criando um objeto de usuário
usuario = Usuario(
    nome="Gabriel Roman",
    idade=30,
    cor="Branco",
    genero="Masculino",
    estado_civil="Solteiro",
    usuario="gabrielroman",
    senha="gabriel123",
    renda_mensal=5000.00
)

# Inicializando a aplicação Flet
ft.app(target=lambda page: tela_de_login(page, usuario))
