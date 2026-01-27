class Passaro:
    def voar(self): 
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
       super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

def plano_de_voo(objeto_passaro):
    objeto_passaro.voar()



p1 = plano_de_voo(Pardal())
p2 = plano_de_voo(Avestruz())

