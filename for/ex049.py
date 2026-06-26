termo = int(input('Digite o primeiro termo: '))
razao = int(input('A razão: '))
for posicao in range (1, 11):
    proximo_termo = termo + (posicao -1) * razao
    print(proximo_termo)