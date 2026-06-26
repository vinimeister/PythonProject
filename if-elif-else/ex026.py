from random import randint
from time import sleep
numero = int(input('Escolha um número de 0 a 100: '))
print('PROCESSANDO')
sleep(1)
numero_secreto= randint (0,100)
if numero == numero_secreto:
    print(f'você acertou o número, era o número {numero_secreto}')
else:
    print(f'você errou, era o número {numero_secreto}, tente novamente!')
