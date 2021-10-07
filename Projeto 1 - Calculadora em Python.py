def soma(n1, n2):
    print('Resultado: ', n1 + n2)

def subtracao(n1, n2):
    print('Resultado: ', n1 - n2)

def multiplicacao(n1, n2):
    print('Resultado: ', n1 * n2)

def divisao(n1, n2):
    print('Resultado: ', n1 / n2)

titulo = 'CALCULADORA EM PYTHON'
resp = 'S'

while True:
    if resp != 'S':
        break
    else:
        print(f'{titulo.center(40, "*")}')
        print('Selecione o número da operação desejada: ')
        print('-'*40)
        print('1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão')
        print('-'*40)
        esc = int(input('Digite sua opção (1/2/3/4): '))
        print('-'*40)
        n1 = float(input('Digite o primeiro número: '))
        print()
        n2 = float(input('Digite o segundo número: '))
        print('-'*40)
        if esc == 1:
            soma(n1, n2)
        if esc == 2:
            subtracao(n1, n2)
        if esc == 3:
            multiplicacao(n1, n2)
        if esc == 4:
            divisao(n1, n2)
        resp = str(input('Quer tentar novamente? [S/N]: ')).strip().upper()
