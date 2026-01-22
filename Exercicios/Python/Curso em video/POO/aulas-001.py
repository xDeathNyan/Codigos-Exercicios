# Declaração de classe
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Guilherme"
g1.idade = 23
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Letícia"
g2.idade = 24
g2.aniversario()
print(g2.mensagem())
