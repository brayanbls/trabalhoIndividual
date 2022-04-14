class Categoria:

    def __init__ (self, cod = None, nomeCat = None):
        self.codigo = cod
        self.nome = nomeCat

    def Cadastrar(self):
        print("Código: "),self.codigo
        print("Nome: ",self.nome)
        print("Categoria cadastrada com sucesso!")