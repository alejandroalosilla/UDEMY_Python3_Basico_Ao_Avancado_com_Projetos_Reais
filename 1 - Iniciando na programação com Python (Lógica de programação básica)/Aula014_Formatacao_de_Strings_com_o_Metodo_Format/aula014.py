a = 'A'
b = 'B'
c = 1.1
d = 'D'
string = 'd={3} a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c, d)
print(formato)

n1 = 'Marcos'
n2 = 'Beto'
n3 = 'Marcia'

lista_nomes = '1º Nome = {nome1} 2º Nome = {nome2} 3º Nome = {nome3}'
form = lista_nomes.format(nome1=n1, nome2=n2, nome3=n3)
print(form)
