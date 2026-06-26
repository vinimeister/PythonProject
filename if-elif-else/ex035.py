#convertando o numero para binário, octal e hexadecimal

numero = int(input('digite o número: '))
print('Escolha a base para conversão: ')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')

opcao = int(input('digite sua opção 1/2/3: '))

if opcao == 1:
    resultado = bin(numero)[2: ]
    print(f'O número {numero} em binário é: {resultado}')
elif opcao == 2:
    resultado = oct(numero)[2: ]
    print(f'O número {numero} em octal é: {resultado}')
elif opcao == 3:
    resultado = hex(numero)[2: ]
    print(f'O número {numero} em hexadecimal é : {resultado}')
else:
    print('Opção invalida! escolha 1, 2 ou 3.')