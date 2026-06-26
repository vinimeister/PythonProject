soma =0
for contador in range(0,6):
    valor = int(input('Digite os números:'))
    if valor % 2 ==0:
        soma += valor
    else:
        print('não considero número impar na soma.')
print(f'a soma dos números pares é {soma}')