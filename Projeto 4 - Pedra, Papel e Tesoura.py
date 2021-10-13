import random

vit_usu = 0
vit_pc = 0
empate = 0

opções = ['pedra','papel','tesoura']

print('SEJAM BEM-VINDOS AO PEDRA, PAPEL E TESOURA!')
print()

while True:
    ent_usu = input('Digite Pedra/Papel/Tesoura ou E para sair: ').lower()
    if ent_usu == 'e':
        break

    if ent_usu not in opções:
        continue

    num_random = random.randint(0, 2)
    # pedra: 0, papel: 1 e tesoura: 2
    esc_pc = opções[num_random]
    print(f'O computador escolheu {esc_pc}.')

    if ent_usu == 'pedra' and esc_pc == 'tesoura':
        print('Você venceu!')
        vit_usu += 1
    elif ent_usu == 'tesoura' and esc_pc == 'papel':
        print('Você venceu!')
        vit_usu += 1
    elif ent_usu == 'papel' and esc_pc == 'pedra':
        print('Você venceu!')
        vit_usu += 1
    elif ent_usu == esc_pc:
        print('Foi um empate!')
        empate += 1
    else:
        print('Você perdeu!')
        vit_pc += 1

print(f'Você venceu {vit_usu} vezes.')
print(f'O computador venceu {vit_pc} vezes.')
print(f'{empate} empate(s) entre você e o computador.')
print()
print('Até a próxima!')