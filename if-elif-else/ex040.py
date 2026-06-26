#calculando se forma triangulo, se é igual ou não.

reta1 = int(input('reta1: '))
reta2 = int(input('reta2: '))
reta3 = int(input('reta3: '))

if reta1 < reta2 +reta3 and reta2 < reta1 + reta3 and reta3 <reta1 + reta2:
    forma= True
else:
    forma = False
if forma:
    print('Forma triangulo')
    if reta1 == reta2 and reta2 == reta3:
        print('é Equilátero')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não forma')