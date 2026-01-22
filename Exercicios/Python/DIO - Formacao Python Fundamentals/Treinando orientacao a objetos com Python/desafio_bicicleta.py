class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def __str__(self):
        return f"Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: R$ {self.valor:,.2f}"
    
    def buzinar(self):
        print("Buzina: plim plim!")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("A bicicleta está em movimento.")
    


b1 = Bicicleta("Vermelha", "Mountain Bike", 2021, 1500.00)
print(b1)

