#maquina de cartão
valor = float(input('Valor a ser pago: '))
print("qual a condição de pagamento?")
print('1 - Dinheiro')
print('2 - Cheque')
print('3 - Cartão')
dinheiro = valor - (valor * 10 / 100)
cheque = valor - (valor * 10 / 100)
cartao = valor - (valor * 5 / 100)

pagamento = int(input('digite sua opção 1/2/3: '))

if pagamento == 1:
    print('Você tem 10% de desconto')
    print(f'valor a ser pago R${dinheiro}')
elif pagamento == 2:
    print('Você tem 10% de desconto')
    print(f' valor a ser pago R${cheque}')
elif pagamento == 3:
    print('você desejaria parcelar?')
    print('1 - À vista')
    print('2 - 2x')
    print('3 - 3x')
    print('4 - 4x')
    print('5 - 5x')
    print('6 - 6x')
    print('7 - 7x')
    print('8 - 8x')
    print('9 - 9x')
    print('10 - 10x')
    print('11 - 11')
    print('12 - 12x')
    pagamento = int(input('1/2/3/4: '))

    if pagamento == 1:
        print('Você tem 5% de desconto à vista')
        print(f'valor a ser pago R${cartao}')
    elif pagamento == 2:
        parcela = valor / 2
        print(f'sem descontos! ficará {valor}')
        print(f'você pagará 2x de {parcela}')

    elif pagamento == 3:
        parcela = valor / 3
        print(f'você pagará 3x de {parcela}')
    elif pagamento == 4:
        parcela = valor / 4
        print(f'você pagará 4x de {parcela}')
    elif pagamento == 5:
        parcela = valor / 5
        print(f'você pagará 5x de {parcela}')
    elif pagamento == 6:
        parcela = valor / 6
        print(f'você pagará 6x de {parcela}')
    elif pagamento == 7:
        parcela = valor / 7
        print(f'você pagará 7x de {parcela}')
    elif pagamento == 8:
        x = valor + (valor * 20 / 100)
        parcela = x / 8
        print(f'você pagará 20% de juros R${x}')
        print(f'você pagará 8x de {parcela}')
    elif pagamento == 9:
        x = valor + (valor * 20 / 100)
        parcela = x / 9
        print(f'você pagará 20% de juros R${x}')
        print(f'você pagará 9x de {parcela}')
    elif pagamento == 10:
        x = valor + (valor * 20 / 100)
        parcela = x / 10
        print(f'você pagará 20% de juros R${x}')
        print(f'você pagará 10x de {parcela}')
    elif pagamento == 11:
        x = valor + (valor * 20 / 100)
        parcela = x / 11
        print(f'você pagará 20% de juros R${x}')
        print(f'você pagará 11x de {parcela}')
    elif pagamento == 12:
        x = valor + (valor * 20 / 100)
        parcela = x / 12
        print(f'você pagará 20% de juros R${x}')
        print(f'você pagará 12x de {parcela}')




