lista = list()
pares = list()
impares = list()
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    if numero % 2 == 1:
        impares.append(numero)
    final = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if final == 'S':
        continue
    if final == 'N':
        break
    if final != 'S' or final != 'N':
        continuar = input('Opção inválida! digite novamente [S/N]: ').upper().strip()[0]
        continue
print(f'A lista completa é {lista}')
print(f'os valores pares são: {pares}')
print(f'os valores ímpares são: {impares}')
