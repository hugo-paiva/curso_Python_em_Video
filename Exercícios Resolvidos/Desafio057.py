sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in "FM":
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))