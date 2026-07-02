from random import randint
vitoria= 0
while True:
    valor_bot = randint(0, 10)
    valor= int(input('Digite um valor: '))
    escolha = str(input('par ou impar?: ')).upper().strip()
    if escolha != 'PAR' and escolha != 'IMPAR':
        print('Opção inválida')
        continue

    valor_total = valor+valor_bot
    print(f'o bot escolheu {valor_bot}')
    print(f'a soma total deu {valor_bot+valor}')
    par = (valor + valor_bot) % 2 == 0
    if escolha == 'PAR' and par:
        vitoria+=1
        print(f'Você ganhou e tem {vitoria} pontos.')
    elif escolha == 'IMPAR' and par == False:
        vitoria+=1
        print(f'Você ganhou e tem {vitoria} pontos.')
    else:
        print('Você perdeu')
        break

print(f'você pontuou {vitoria} vezes')


