from math import factorial
flag = True
while flag:
    numero = int(input('Digite seu número: '))
    print(factorial(numero))
    ten= str(input('Você deseja continuar? [S/N]: '))
    if ten == 'n':
        flag = False