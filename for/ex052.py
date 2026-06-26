from datetime import date

print('Aqui mostramos se você já é maior de idade ou não.')
for quantidade in range(1,7):
    atual = date.today().year
    data_nascimento = int(input('Digite sua data de nascimento: '))
    idade = atual - data_nascimento
    if idade <= 17:
        saldo = 18 - idade
        print(f'Você tem {idade} anos e faltam {saldo} anos para ser maior de idade.')

    else:
        print(f'você tem {idade} e é maior de idade.')