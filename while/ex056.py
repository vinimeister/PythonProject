from random import randint
from time import sleep
numero1= int(input('Escolha seu número de 0 à 10: '))
print('PROCESSANDO!')
sleep(0.5)
numero_secreto = randint(0, 10)
tentativa = 1
while numero1 != numero_secreto:
    if numero1 < numero_secreto:
        print('O número é MAIOR que isso!')
    else:
        print('O número é MENOR que isso!')
    numero1 = int(input('Você errou, tente novamente de 0 à 10:  '))
    print('PROCESSANDO!')
    sleep(0.5)
    tentativa += 1
print(f'Você acertou o número {numero1} em {tentativa} tentativas!')

