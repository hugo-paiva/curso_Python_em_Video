nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
primeiro = nome.split()[0]
#len = len(primeiro)
# Ou mais facilmente
len = nome.find(' ')

print('Seu primeiro nome é {} e ele tem 5 letras.'.format(primeiro, len))
