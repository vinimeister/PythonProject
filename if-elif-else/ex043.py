#jogo jokenpô
escolha1 = input('Escolha entre Pedra, Papel ou Tesoura: ')
escolha2= input('Escolha novamente: ')
regras = dict(pedra='pedra', tesoura='tesoura', papel='papel')


if regras[escolha1] == regras[escolha2]:
    print('Empate')
else:
    if escolha1 =='papel' and escolha2 =='pedra':
        print(f'o jogador 1 botou {escolha1} e venceu!')
    elif escolha1=='pedra' and escolha2 =='tesoura':
        print(f'o jogador 1 botou {escolha1} e venceu!')
    elif escolha1 =='tesoura' and escolha2 =='papel':
        print(f'o jogador 1 botou {escolha1} e venceu!')
    else:
        print(f'o jogador 2 botou {escolha2} e venceu!')
