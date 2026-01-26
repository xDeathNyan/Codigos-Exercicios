class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return "\n".join([f"{k.upper():>15}: {v}" for k, v in vars(self).items()])


class Mamifero(Animal):
    def __init__(self, nro_patas, cor_pelo="Indefinida"):
        super().__init__(nro_patas)


class Ave(Animal):
    def __init__(self, nro_patas):
        super().__init__(nro_patas)



class Gato(Mamifero):
    pass



class Ornitorrinco(Mamifero, Ave):
    pass



gato = Gato(4, "Laranja")
print(gato)