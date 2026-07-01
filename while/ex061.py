numero = int(input('Digite o valor de n: '))
anterior= 0
atual = 1
contador = 2
if numero > 0:
    print(anterior, end=' → ')
if numero > 1:
    print(atual, end=' → ')

while contador < numero:
    calculo_proximo = atual + anterior
    anterior = atual
    atual = calculo_proximo
    print(calculo_proximo, end=' → ')
    contador += 1
print('FIM')