a = int(input('Quantos dias alugados?: '))
rodados = float(input('Quantos Km rodados?: '))
dia = 60 * a
km = 0.15 * rodados
print(f'o total a pagar é R${dia+km}')