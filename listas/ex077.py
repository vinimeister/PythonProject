valores = list()
while True:
    numero= int(input('Digite um valor: '))
    if numero in valores:
        print(f'O número {numero} já existe na lista')
    else:
        valores.append(numero)
        print(f'Número {numero} foi adicionado na lista')
    final = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if final == 'S':
        continue
    if final == 'N':
       break
    if final != 'S' or final != 'N':
        print('Opção inválida, digite Sim para continuar ou Não para finalizar.')
        continuar = input('Deseja continuar?: [S/N]: ').upper().strip()[0]
        continue
valores.sort()
print(f'Os valores adicionados foram: {valores}')