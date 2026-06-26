#alistamento militar#
from datetime import date
atual = date.today().year
nascimento= int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print(f'você nasceu em {nascimento} e tem {idade} em {atual}')
if idade== 18:
    print('Você tem que se alistar neste ano.')
elif idade< 18:
    saldo = 18 - idade
    print(f'você ainda não precisa se alistar, ainda faltam {saldo} anos pra se alistar.')
    ano = atual + saldo
    print(f'seu alistamento será em {ano}')
elif idade> 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')

