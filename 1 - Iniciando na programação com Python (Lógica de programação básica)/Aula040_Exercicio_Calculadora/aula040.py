""" Calculadora com while """
from time import sleep

print('#### CALCULADORA ####')
print('----------------------')

while True:
    r = 0
    r2 = ''
    while True:
        try:
            n1 = float(input('\nDigite o primeiro valor: '))
            n2 = float(input('Digite o segundo valor: '))
            break
        except ValueError:
            print("Por favor digite um valor válido!")
            sleep(2)
            continue

    while True:
        op = input('''\nEscolha um operador:
-------------
[+] 
[-]
[*]
[/]
>>> ''').strip()
        
        if op in ('+', '-', '*', '/'):
            break
        else:
            print('Selecione umas das opções! Por favor!')
            sleep(2)
            continue

    if op == '+':
        r = n1 + n2
        r2 = 'soma'
    elif op == '-':
        r = n1 - n2
        r2 = 'subtração'
    elif op == '*' :
        r = n1 * n2
        r2 = 'multiplicação'
    elif op == '/':
        r = n1 / n2
        r2 = 'divisão'

    print(f'\nO resultado da {r2} é : {r}')
    sleep(2)

    while True:
        p = input('\nQuer sair ? [s/n]: ').strip().lower()

        if p in ('s', 'n'):
            break
        else:
            print('Por favor! Escolha "s" ou "n" !')
            sleep(2)
            continue

    if p == 's':
        break
    else:
        continue
print('\nAté mais!')
print('Fechando...')
sleep(2)
