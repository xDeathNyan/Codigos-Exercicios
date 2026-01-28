'''
Funções em Python são objetos de primeira classe. Isso significa que as funções podem ser passadas
e usadas como argumentos.

É possível definir funções dentro de outras funções . Tais funções são chamadas de funções internas.
'''

def dizer_oi(nome):
    return f'Oi {nome}!'

def incentivar_aprender(nome):
    return f'Vamos aprender Python, {nome}!'

def mensagem_personalizada(funcao, nome):
    return funcao(nome)


print(mensagem_personalizada(dizer_oi, 'Maria'))
print(mensagem_personalizada(incentivar_aprender, 'João'))  

def pai():
    print("Escrevendo a função pai")

    def filho1():
        print("Escrevendo a função filho 1")

    def filho2():
        print("Escrevendo a função filho 2")

    filho1()
    filho2()

pai()