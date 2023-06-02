"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('O número digitado será dobrado: ')

try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um número!')
