total_mulheres = maiores = homens = 0

while True:
    nome = str(input('Qual o seu nome?: '))
    idade = int(input('Qual a sua idade?: '))


    while True:
        print('Qual o seu sexo?')
        print('1 - Masculino')
        print('2 - Feminino')
        sexo = int(input('1/2: '))

        if sexo == 1 or sexo == 2:
            break
        else:
            print('Opção inválida! Digite 1 para Masculino ou 2 para Feminino.')

    if idade >= 18:
        maiores += 1
    if sexo == 2 and idade < 20:
        total_mulheres += 1
    if sexo == 1:
        homens += 1

    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'S s SIM':
        continue
    if continuar == 'N n NÃO':
        break
    if continuar != 'S' or continuar != 'N':
        print('Opção inválida, digite Sim para continuar ou Não para finalizar.')
        continuar=input('Deseja continuar?: [S/N]: ')
        continue

print(f'tem {maiores} maiores de 18 anos.')
print(f'houve {homens} homens registrados.')
print(f'tem {total_mulheres} mulheres menos de 20 anos.')