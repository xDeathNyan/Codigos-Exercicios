'''
Python também permite que você use funções internas como retorno de outras funções.
'''

def calcular(operacao):
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    if operacao == 'soma':
        return soma
    else:
        return subtracao
    
resultado = calcular('soma')(5, 3)
print(resultado)  # Saída: 8
resultado = calcular('subtracao')(5, 3)
print(resultado)  # Saída: 2
