#se forma um triangulo com as retas

reta1 = int(input('reta1: '))
reta2 = int(input('reta2: '))
reta3 = int(input('reta3: '))

if reta1 < reta2 + reta3:
    if reta2 < reta1 + reta3:
        if reta3 < reta1 + reta2:
            forma =  True
        else:
            forma = False
    else:
        forma = False
else:
    forma = False
if forma:
    print('Forma triangulo')
else:
    print('Não forma')