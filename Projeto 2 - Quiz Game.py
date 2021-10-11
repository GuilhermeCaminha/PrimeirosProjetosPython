print('SEJAM BEM-VINDOS AO MEU QUIZ!')
jogar = str(input('Você deseja jogar? [S/N]: '))
if jogar.strip().upper() != 'S':
    quit()

print('Ótimo. Vamos jogar!')
pontuacao = 0

resp = str(input('O que significa a sigla "CPU" em português? '))
if resp.lower() == 'unidade de processamento central':
    print('Correto!')
    pontuacao += 1
else:
    print('Incorreto!')

resp = str(input('O que significa a sigla "GPU" em português? '))
if resp.lower() == 'unidade de processamento gráfico':
    print('Correto!')
    pontuacao += 1
else:
    print('Incorreto!')

resp = str(input('O que significa a sigla "RAM" em português? '))
if resp.lower() == 'memória de acesso aleatório':
    print('Correto!')
    pontuacao += 1
else:
    print('Incorreto!')

resp = str(input('O que significa a sigla "PSU" em português? '))
if resp.lower() == 'unidade de fonte de alimentação':
    print('Correto!')
    pontuacao += 1
else:
    print('Incorreto!')

print('Você conseguiu ' + str(pontuacao) + ' questões corretas!')
print('Você conseguiu ' + str((pontuacao/4)*100) + '% de acertos!')