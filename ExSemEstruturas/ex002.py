idade = int(input("Digite sua idade: "))

if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"Você é classificado como: {categoria}")