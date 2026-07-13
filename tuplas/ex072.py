from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f' os número gerados foram {numeros}')
maior = max(numeros)
menor = min(numeros)
print(f'o maior foi {maior} e o menor foi {menor}')
