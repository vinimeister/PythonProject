numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
contador = int(input('Digite o número de 0 a 20: '))

while contador < 0 or contador > 20:
    contador = int(input('Opção inválida! digite um número entre 0 e 20: '))

print(f'Você digitou o número {numero[contador]}')
