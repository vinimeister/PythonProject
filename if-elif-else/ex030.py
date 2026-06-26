#programa que lê número bissexto

ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'{ano} é um ano BISSEXTO')
        else:
            print(f'{ano} Não é um ano BISSEXTO')
    else:
        print(f'{ano} é um ano BISSEXTO')
else:
    print(f'{ano} NÃO é um ano BISSEXTO')