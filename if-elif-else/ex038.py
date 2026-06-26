#ajudando os professores

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
soma = (nota1+nota2) /2
if soma < 5.0:
    print(f'sua nota é {soma}')
    print('Reprovado!')
elif soma <= 6.9:
    print(f'sua nota é {soma}')
    print('Recuperação')
else:
    print(f'Sua nota é {soma}')
    print('Aprovado!')