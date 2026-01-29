'''
Inner functions (funções internas)
É possível definir funções dentro de outras funções.
'''
def pai():
    print("Escrevendo a função pai")

    def filho1():
        print("Escrevendo a função filho 1")

    def filho2():
        print("Escrevendo a função filho 2")

    filho1()
    filho2()

pai()
