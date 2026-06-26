numero = int(input('Digite um número: '))
tot = 0
for i in range(1, numero + 1):
    if numero % i ==0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{i} ', end='')
print(f'\n\033[mO Número {numero} foi divisível {tot} vezes.')
if tot ==2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')