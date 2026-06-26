tabuada = int(input('Digite seu número: '))
print('Sua tabuada é:')
for contador in range (1,11):
     numerotabuada= tabuada * contador
     print(f'{tabuada}x{contador}={numerotabuada}')
