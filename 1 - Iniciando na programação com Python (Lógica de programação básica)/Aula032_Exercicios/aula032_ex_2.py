"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora atual: ')

try:
    hora = int(hora)
    if hora in range(0, 24):
        if 0 <= hora <= 11:
            print('Bom dia!')
        elif 12 <= hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
    else:
        print('Digite um número inteiro entre 0 e 24.') 
except:
    print('Digite um valor inteiro entre 0 e 24.')
 