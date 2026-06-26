import math
num = float(input('comprimento do cateto oposto: '))
num1 = float(input('comprimento do cateto adjcente: '))
hi = math.hypot(num, num1)
print(f'A Hipotenusa é {hi}')
