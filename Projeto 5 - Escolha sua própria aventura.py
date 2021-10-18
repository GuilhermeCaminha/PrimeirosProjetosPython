print('SEJAM BEM-VINDOS AO JOGO DE AVENTURA!')
morte = 'Um dragão surge das nuvens acima de você. Voa em sua direção. Uma luz surge do fundo de sua garganta. ' \
        'Uma rajada de chamas infernais cai sobre você. VOCÊ MORREU!'
while True:
    nome = str(input('Qual é o seu nome? '))
    print(f'Seja bem-vindo {nome}!')
    resp = str(input('Você está em uma estrada empoeirada, ela chega ao fim, você pode escolher direita ou esquerda. Qual '
                     'caminho você escolhe? [direita/esquerda]: ')).lower()
    if resp == 'esquerda':
        resp = str(input('Você desceu até um barrando, na beira do rio, você pode andar até uma área mais rasa ou tentar'
                         ' nadar. Qual você escolhe? [andar/nadar]: ')).lower()
        if resp == 'andar':
            resp = str(input('Você encontra na lateral do rio um baú, levemente enterrado na areia, você deseja forçar'
                             ' a abertura ou deixar ele lá? [abrir/deixar]: ')).lower()
        elif resp == 'nadar':
            resp = str(input('Você vê, no fundo do rio, um baú, você deseja tentar alcançar o baú, ou apenas atravessa'
                             ' o rio? [alcançar/atravessar]: ')).lower()
        else:
            print(morte)
            print(f'Obrigado por jogar {nome}!')
            break
    elif resp == 'direita':
        resp = str(input('Você vê uma cabana ao final de uma descida, ao lado da estrada, você bate na porta ou chama por'
                         ' alguém? [bater/chamar]: ')).lower()
        if resp == 'bater':
            resp = str(input('Você bate na porta. Ouve um barulho de objetos caindo no interior da cabana. Uma mulher de'
                             ' aparência macabra abre as portas gritando: "VOCÊ ME FEZ DESTRUIR MEU FEITIÇO!". Ela parte '
                             'para cima de você. Você se defende ou foge? [atacar/fugir]: ')).lower()
        elif resp == 'chamar':
            resp = str(input('Uma senhora abre a porta. Ela veste uma capa escura, escondendo o rosto atrás de um capuz.'
                             ' Ela diz que há muito tempo ninguém aparecia em sua casa. Ela pede para você entrar. Você '
                             'entra ou foge? [entrar/fugir]: ')).lower()
        else:
            print(morte)
            print(f'Obrigado por jogar {nome}!')
            break
    else:
        print(morte)
        print(f'Obrigado por jogar {nome}!')
        break