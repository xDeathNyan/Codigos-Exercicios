class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(50)
conta.sacar(30)
#conta._saldo += 50 # Tentativa de acesso direto ao atributo protegido (não recomendado)
#print(conta._saldo)  # Acesso direto ao atributo protegido (não recomendado fora da classe ou subclasses)
print(conta.nro_agencia)  # Acesso ao atributo público
print(conta.mostrar_saldo())  # Acesso ao saldo via método público (recomendado)