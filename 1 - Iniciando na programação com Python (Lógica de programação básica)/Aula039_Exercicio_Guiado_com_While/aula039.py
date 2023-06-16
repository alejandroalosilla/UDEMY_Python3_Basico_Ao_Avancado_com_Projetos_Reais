"""
Iterando strings com while
"""
nome = 'Luiz Otávio'  # Iteráveis

i = 0
novo_nome = ''

while i < len(nome):
    novo_nome += f'*{nome[i]}'
    i += 1

print(novo_nome)
