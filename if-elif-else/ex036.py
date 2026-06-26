#verificando se o numero é maior, menor ou igualx

numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite o segundo número: '))
if numero1 >numero2:
    print(f'O {numero1} é maior que {numero2}')
elif numero2 > numero1:
    print(f'O {numero2} é maior que {numero1}')
else:
    print('Não existe valor maior, os dois são iguais')