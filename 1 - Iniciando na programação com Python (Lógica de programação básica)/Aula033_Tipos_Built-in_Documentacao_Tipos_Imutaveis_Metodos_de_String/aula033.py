"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""



string = 'Luiz Otávio'

# string[3] = 'ABC' -> Daria erro, pois str é imutável
# Forma alternativa(gambiarra):
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
# Método .zfill() preenche com zeros uma determinada _width á esquerda da variável string"
print(string.zfill(10))
