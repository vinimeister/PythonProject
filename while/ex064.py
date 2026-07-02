numero = soma =0
while True:
    numero = int(input('Digite o número: '))
    if numero == 999:
        break
    soma += numero
print(f'a soma dos números foi {soma}')