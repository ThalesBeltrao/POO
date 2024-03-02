# class - Classes sao moldes para criar novos objetos
# as classes geram novos objetos(instancias)
# podem ter seus proprios atributos(dados) e metodos(ações)
# Os objetos geradsos pela classe podem usar seus dados
# internos para realizar varias ações
# por conveção, usamsos PascalCase para nomes de
# classes


class Pessoa:
    ...

p1 = Pessoa()
p1.nome = "luiz"
p1.sobrenome = "Otavio"
print(p1.nome,end=" ")
print(p1.sobrenome)
print()

# __init__ inicializador de objeto
class Pessoa:
    def __init__(self, nome, sobrenome): # self ele é a variael p1 fora da classe
        self.nome = nome
        self.sobrenome = sobrenome

#p1 = Pessoa("thales", "wilian")

print(p1.nome, p1.sobrenome)

#repara que nesse caso só tem parametros não temos metodos a sua classe não executa nenhuma ação ()