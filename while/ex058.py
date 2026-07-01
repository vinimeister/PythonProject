numero = int(input('digite um número para o calculo fatorial: '))
contador = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while contador > 0:
    print(f'{contador}', end ='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print(fatorial)