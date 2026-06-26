#programa que calcula o preço da viagem até 200km por 50 centavos e viagens mais de 200km por 45 centavos

km_viagem = 200
distancia = int(input('Qual a distância da sua viagem?: '))
if distancia <= km_viagem:
    preco = distancia * 0.5
    print(f'você paga R${preco}')
else:
    preco = distancia * 0.45
    print(f'como sua viagem é mais longa, terá desconto e pagará R${preco}')