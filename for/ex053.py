print('Aqui veremos quem tem o maior peso e o menor.')
maior = 0
menor = 0
for i in range(0,5):
    peso = float(input(f'Digite o peso {i+1} da pessoa: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso >maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}Kg')
print(f'O menor peso foi {menor}kg')