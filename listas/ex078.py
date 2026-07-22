lista = []
for contador in range(5):
    numero = int(input('Digite um valor:'))

    posicao = 0
    while posicao < len(lista) and lista[posicao] < numero:
        posicao +=1

    lista.insert(posicao, numero)
    print(f'Inserido na posição {posicao}')
print(f'Lista ordenada: {lista}')