soma = 0
cont = 0
for contador in range(1,501,2):
  if contador % 3 == 0:
        soma += contador
        cont += 1
print(f'a soma de todos os {cont} valores solicitados é {soma}')