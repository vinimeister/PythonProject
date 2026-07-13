
tupla = (int(input('Digite um número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))

print(f'Tupla digitada: {tupla}')
print('-' * 40)
print(f'A) O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'B) O primeiro 3 está na posição {tupla.index(3)}')
else:
    print('B) O valor 3 não foi digitado.')

pares = [num for num in tupla if num % 2 == 0]
if pares:
    print(f'C) Os números pares são: {pares}')
else:
    print('C) Não foram digitados números pares')