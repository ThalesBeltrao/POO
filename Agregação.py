class Carrinho:
    def __init__(self):
        self._produto = []

    def somar(self):

        return f"Valor total dos produtos R$:{sum(p.valor for p in self._produto)}"# list comprehension

    def add_produto(self, *produto): # o atributo produto recebe as instancias da classe Produto e joga dentro deles os seus atributos na lista
        self._produto.append(*produto)


    def listar_produto(self):
        for i in self._produto:
            print("{},R$:{}".format(i.nome, i.valor))

    def cont_list(self):
        return f"Você tem {len(self._produto)} produtos no carrinho"



class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor



cerveja = Produto("sckol", 4.00)
bolo = Produto("coco", 2.80)
refrigerante = Produto("coca-cola", 9.80)
carrinho = Carrinho()
carrinho.add_produto(cerveja)
carrinho.add_produto(bolo)
carrinho.add_produto(refrigerante)
carrinho.listar_produto()
print(carrinho.cont_list())
print(carrinho.somar())

# A gregação é uma especialização da associação
# eu tentei trazer de uma maneira simplificada usando apenas um aquivo
# para a didatica é interessante
