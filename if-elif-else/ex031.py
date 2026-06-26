#numero maior e o menor

numero1 = int(input('Digite o número: '))
numero2 = int(input('Digite o número: '))
numero3 = int(input('Digite o número: '))
maior = numero1
menor = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
print(f'O número {maior} é o maior e o menor é {menor}')
