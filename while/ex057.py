from time import sleep
valor1= int(input('Digite seu valor: '))
valor2= int(input('Digite seu valor: '))


opcao =0
while opcao != 5:
    print(f'Os valores atuais: {valor1} e {valor2}')
    print('''[1]- Somar
[2]- Multiplicar
[3]- Maior
[4]- Novos Números
[5]- Sair do programa''')
    opcao = int(input('Digite sua opção 1/2/3/4/5: '))
    if opcao ==1:
     somar = valor1 + valor2
     print(f'A soma foi dos seus valores foi {somar}')
    elif  opcao ==2:
        multiplicar = valor1 * valor2
        print(f'A multiplicação dos valores foi {multiplicar}')
    elif opcao ==3:

        if valor1 > valor2:
            print(f'O {valor1} é maior que o {valor2}')
        elif valor1 == valor2:
            print('O Valor é o mesmo!')
        else:
            print(f'O {valor2} é maior que o {valor1}')
    elif opcao ==4:
        valor1 = int(input('Digite seu valor: '))
        valor2 = int(input('Digite seu valor: '))
        print('Valores atualizados!')
    elif opcao ==5:
        print('Obrigado por usar meu programa! :)')

    else:
        print('Opção inválida!')

    sleep(1)