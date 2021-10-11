import random

print('SEJAM BEM-VINDOS AO JOGO DE ADIVINHAÇÃO!')
jogar = str(input('Você deseja jogar? [S/N]: '))
if jogar.strip().upper() != 'S':
    quit()
print()
print('Digite abaixo um número limite para o jogo:')
print('Lembre-se que o jogo irá de zero ao número digitado!')
print()
n_maximo = input('Digite um número: ')

if n_maximo.isdigit():
    n_maximo = int(n_maximo)
    if n_maximo <= 0:
        print('Por favor, digite um número maior que zero na próxima!')
        quit()
else:
    print('Por favor, digite um número na próxima!')

n = random.randint(0, n_maximo)
tentativas = 0
print()
while True:
    tentativas += 1
    resp_jog = input('Tente adividar o número: ')
    if resp_jog.isdigit():
        resp_jog = int(resp_jog)
    else:
        print('Por favor, digite um número na próxima!')
        continue
    if resp_jog == n:
        print('Você acertou!')
        break
    elif resp_jog > n:
        print('Você está acima do número!')
        print()
    else:
        print('Você está abaixo do número!')
        print()
print()
print(f'Você precisou de {tentativas} tentativas!')