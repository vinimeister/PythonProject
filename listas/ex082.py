galera = list()
lista = list()
pesos =  list()
while True:
    nome = str(input('Digite o seu nome: '))
    peso = int(input('Digite o seu peso: '))
    lista.append(nome)
    lista.append(peso)
    galera.append(lista[:])
    pesos.append(peso)
    lista.clear()
    while True:
            final = input('Quer continuar? [S/N]: ').upper().strip()[0]
            if final =='S' or final =='N':
                break
            print('Opção inválida! tente novamente')

    if final =='N':
        break
print(f'O total de {len(galera)} pessoas foram cadastradas.')

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'Pessoas mais pesadas são {maior_peso}kg.')
for pessoa in galera:
    if pessoa[1] == maior_peso:
        print(f' {pessoa[0]}')
print(f'As pessoas mais leves são {menor_peso}kg.')
for pessoa in galera:
    if pessoa[1] == menor_peso:
        print(f' {pessoa[0]}')
