'''
O decorador pode decidir se retorna o valor da função decorada ou não. Para que o valor seja retornado,
a função envelope deve retornar o valor da função decorada.
'''

def duplicar_com_retorno(func): 
    def envelope(*args, **kwargs): 
        func(*args, **kwargs)  # Chama a função original
        return func(*args, **kwargs)  # Retorna o resultado duplicado
    
    return envelope

@duplicar_com_retorno
def aprender_com_retorno(tecnologia): 
    print(f'Estou aprendendo {tecnologia}!')
    return tecnologia.upper()

tecnologia = aprender_com_retorno('Python')
print(tecnologia)  # Saída: PYTHON