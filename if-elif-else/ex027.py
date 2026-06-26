#verificando multa por excesso de velocidade

km_permitido = 80
valor_multa = 7
velocidade = int(input('Qual a velocidade que o carro está?: '))
if velocidade > km_permitido :
    excesso = velocidade - km_permitido
    multa = excesso * valor_multa
    print('\033[31;40mVocê está sendo multado!\033[m')
    print(f'O valor da sua multa é R${multa}')