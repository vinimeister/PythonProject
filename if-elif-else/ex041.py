#calculando IMC
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imca = altura * altura
imcp = peso // imca
print(imcp)
if imcp < 18.5:
    print('Abaixo do peso')
elif imcp <= 24.9:
    print('Peso Normal')
elif imcp <= 29.9:
    print('Sobrepeso')
elif imcp <= 34.9:
    print('Obesidade grau I')
elif imcp <= 39.9:
    print('Obesidade grau II')
else:
    print('Obsidade Mórbida')

if altura <= 1.55:
    print('Seu peso ideal é 44-58kg')
elif altura <= 1.60:
    print('Seu peso ideal é 47-61kg')
elif altura <= 1.65:
    print('Seu peso ideal é 50-61kg')
elif altura <= 1.70:
    print('Seu peso ideal é 54-69kg')
elif altura <= 1.75:
    print('Seu peso ideal é 57-74kg')
elif altura <= 1.80:
    print('Seu peso ideal é 60-78kg')
elif altura <= 1.85:
    print('Seu peso ideal é 64-83kg')
else:
    print('seu peso ideal é 71-89kg')