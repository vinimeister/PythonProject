gasto = quantidade_produto = soma = 0
menor = 9999
nome_do_menor = ''

while True:
    nome = str(input('Qual o nome do produto?: '))
    valor_produto = int(input('Qual o valor do produto?: '))
    soma += valor_produto

    if valor_produto >=1000:
        quantidade_produto+=1
    if valor_produto <menor:
        menor = valor_produto
        nome_do_menor = nome


    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip() [0]
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
    if continuar != 'S' or continuar != 'N':
        print('Opção inválida, digite Sim para continuar ou Não para finalizar.')
        continuar = input('Deseja continuar?: [S/N]: ').upper().strip() [0]
        continue
print(f'A soma de todos os produtos é {soma}')
print(f'A quantidade de produtos que custam mais de R$1000 é {quantidade_produto}')
print(f'O produto de menor valor é {nome_do_menor} que custa R${menor}')