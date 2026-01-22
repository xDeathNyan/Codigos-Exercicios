# Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Método construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de objetos
g1 = Gafanhoto("Guilherme", 23)
print(g1.mensagem())

g2 = Gafanhoto("Letícia", 24)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())  # Valor padrão para nome

print(Gafanhoto.__doc__)  # Documentação da classe
