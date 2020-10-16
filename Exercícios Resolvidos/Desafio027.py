'''nome = str(input('Digite o seu nome completo: ')).strip()
nome = nome.split()
p =nome[0]
nome.reverse()
u = nome[0]
print('Seu primeiro nome é {}'.format(p))
print('Seu último nome é {}'.format(u))'''

#Ou mais facilmente
n = str(input('Digite o seu nome completo:')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
