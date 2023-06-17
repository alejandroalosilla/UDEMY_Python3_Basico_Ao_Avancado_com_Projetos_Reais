""" Calculadora com while """

from time import sleep


def soma(n1, n2):
    return n1 + n2


def subt(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def recebe_num(mensagem):
    while True:
        try:
            num = float(input(mensagem))
            break
        except ValueError:
            print('Por favor, digite um valor válido!')
    return num

def main():

    print('#### Calculadora ####')
    print('---------------------')
    
    while True:
        num1 = recebe_num('Digite o primeiro número: ') 
        num2 = recebe_num('Digite o segundo número: ')
        
        while True:
            op = input("""
[+] Adição
[-] Subtração
[*] Multiplicação
[/] Divisão
[0] Sair
=> """).strip()
            if op in ('+', '-', '/', '=', '0'):
                break
            else:
                print('\nDigite alguma da opções listadas.')
                sleep(2)

        if op == '+':
            print(f'A soma entre {num1} e {num2}: {soma(num1, num2)}')
        elif op == '-':
            print(f'A subtração entre {num1} e {num2}: {subt(num1, num2)}')
        elif op == '*':
            print(f'A multiplicação entre {num1} e {num2}: {mult(num1, num2)}')
        elif op == '/':
            print(f'A divisão entre {num1} e {num2}: {div(num1, num2)}')
        else:
            print('Saindo...')
            sleep(3)
            break
    print('Fim da execução do código.')

main()
