while True:
    valor = int(input('Digite o valor que irá sacar: '))
    restante = valor
    qnt_50 = restante // 50
    restante = restante % 50

    qnt_20 = restante // 20
    restante = restante % 20

    qnt_10 = restante // 10
    restante = restante % 10

    qnt_1 = restante

    if qnt_50 > 0:
        print(f'A quantidade de cédulas de R$50 foram {qnt_50}')
    if qnt_20 > 0:
        print(f'A quantidade de cédulas de R$20 foram {qnt_20}')
    if qnt_10 > 0:
        print(f'A quantidade de cédulas de R$10 foram {qnt_10}')
        if qnt_1 > 0:
            print(f'e as de R$1 foram {qnt_1}')
    print(f'Total de R${valor:.2f} sacado com sucesso!')
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
    if continuar != 'S' or continuar != 'N':
        print('Opção inválida, digite Sim para continuar ou Não para finalizar.')
        continuar = input('Deseja continuar?: [S/N]: ').upper().strip()[0]
        continue