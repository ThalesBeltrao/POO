class Escritor:
    def __init__(self, nome):
        self.nome = nome


class Ferramenta:
    def __init__(self, ferramenta):
        self.ferramenta = ferramenta


    def use_ferramente(self):
        print("{} esta sendo usada".format(self.ferramenta))



escritor = Escritor("thales")
ferramenta = Ferramenta("Caneta")
escritor.ferramenta = ferramenta
escritor.ferramenta.use_ferramente()


# uma associação simples não tem uma relação de dependencia ela
# outro exemplo
print()

class Pessoa:
    def __init__(self, nome):
        self.carro = None
        self.pessoa = nome

    def usar_carro(self, carro):
        self.carro = carro
        print("{} esta sendo usado por {}".format(self.carro, self.pessoa))


class Carro:
    def __init__(self, name, modelo):
        self.carro = name
        self.modelo = modelo



pessoa = Pessoa("thales")
carro = Carro("New Fiesta", "Ford")
pessoa.usar_carro(carro.carro)

