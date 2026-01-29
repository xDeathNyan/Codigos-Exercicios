'''
Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número arbitrário de argumentos
posicionais e de palavras-chave.
'''

def duplicar(func): # Decorador que duplica a execução da função
    def envelope(*args, **kwargs): # Função interna que aceita qualquer número de argumentos
        func(*args, **kwargs)  # Chama a função original
        func(*args, **kwargs)  # Chama a função original novamente
    
    return envelope # Retorna a função interna

@duplicar # Usando o decorador com a sintaxe @
def aprender(tecnologia): 
    print(f'Estou aprendendo {tecnologia}!')


aprender('Python') # Chama a função decorada
aprender('Decoradores')
