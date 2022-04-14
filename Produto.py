class Produto:

    def __init__ (self, cod = None, nomeP = None, precoP = 0.00, qtd = 0):
        self.codigo = cod
        self.nome = nomeP
        self.preco = precoP
        self.qtd = qtd

    def Cadastrar(self):
        print("Código: "),self.codigo
        print("Nome: ",self.nome)
        print("Preco: "),self.preco
        print("Quantidade: ",self.qtd)
        print("Produto cadastrado com sucesso!!")