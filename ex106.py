from time import sleep

c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[7:30m',    # 2 - branco
     )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[0], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)
    print(c[0], end='')
    sleep(1)

# Programa principal:
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)