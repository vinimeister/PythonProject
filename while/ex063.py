resposta = 'Sim, S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Sim, Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade +=1
    if quantidade ==1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar?[S/N]: ')).title().strip() [0]
media = soma / quantidade
print(f'a média dos números é {media}, o maior número é {maior} e o menor é {menor}.')
