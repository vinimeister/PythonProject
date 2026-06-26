#programa que calcula quantos anos ele pagará a casa

casa = int(input('Valor do empréstimo: '))
salario = int(input('O seu Salário: '))
anos = int(input('Quantos anos deseja pagar?: '))
if casa <= 0:
    print('Erro: Valor da casa deve ser maior que zero!')
elif salario <= 0:
    print('Erro: Salário deve ser maior que zero!')
elif anos <= 0:
    print('Erro: Anos deve ser maior que zero!')
else:
    limite = salario * 30 / 100
    meses = anos * 12
    prestacao = round(casa / meses, 2)
    juros = casa * (15 /100)
    print(f'Prestação: R$ {prestacao:.2f}')
    print(f'Limite (30% do salário): R$ {limite:.2f}')
    print(f'O valor total com 15% juros fica R${casa+juros}')
    print(f'O juros ficou em R${juros}')
    if prestacao <= limite:
        print('Aprovado!')
    elif prestacao == limite:
        print('Cuidado - limite máximo!')
    else:
        print('Negado.')