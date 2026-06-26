#codigo que mostra o milimetro e o centimetro de metros

metros = float(input('Digite quantos metros: '))
milimetros =  (metros * 1000)
centimetros = (metros * 100)
print(f'{metros:.0f}m  corresponde a {milimetros:.0f}mm e {metros:.0f}m tem  {centimetros:.0f}cm ')