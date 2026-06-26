masculino = 'Masculino'
feminino = 'Feminino'
sexo = input('Digite seu sexo [Masculino/Feminino]: ').strip().title()
while sexo != masculino and sexo != feminino:
    sexo = input('Dados inválidos. por favor, digite seu sexo novamente [Masculino/Feminino]: ').strip().title()

print(F'Sexo {sexo} registrado com sucesso!')