class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada para {self.titular} com saldo inicial de R$ {self.saldo:,.2f}.\n")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo.\n"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:,.2f} realizado com sucesso na conta {self.id}.\n")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente para saque de R$ {valor:,.2f} na conta {self.id}.\n")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:,.2f} realizado com sucesso na conta {self.id}.\n")





conta1 = ContaBancaria(1, "João", 1000)
conta1.depositar(500)
conta1.sacar(200)
print(conta1)
