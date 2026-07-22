lista = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    lista.sort(reverse=True)
    final = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if final == 'S':
        continue
    if final == 'N':
        break
    lista.append(numero)
print(f'você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print('O 5 não faz parte da lista!')