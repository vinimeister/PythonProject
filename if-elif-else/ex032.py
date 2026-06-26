#mostrando se tem aumento no salario

salario = int(input('Digite seu Salário: '))
if salario > 1250:
    aumento=  salario * ( 10 / 100)
    aumento += salario
else:
    aumento = salario * ( 15 / 100)
    aumento += salario
print(aumento)
