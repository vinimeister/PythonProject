print('Aqui veremos a média de idade, nome do homem mais velho e a mulher que tem menos de 20 anos, caso tenha')
soma_da_idade_total= 0
maior= 0
total_mulheres=0
nome_do_maior=""
for i in range(0,4):
    nome = str(input('Qual o seu nome?: '))
    idade = int(input('Qual a sua idade?: '))
    print('você é masculino ou feminino?')
    print('1- Masculino')
    print('2- Feminino')
    sexo = int(input('1/2: '))
    soma_da_idade_total += idade
    if idade > maior:
        maior = idade
        nome_do_maior=nome
    if sexo == 2:
        if idade < 20:
            total_mulheres += 1



media = soma_da_idade_total / 4
print(f'a média de idade dos 4 é {media}')
print(f'O mais velho é o {nome_do_maior}.')
print(f'O total de mulheres abaixo de 20 é {total_mulheres}')
