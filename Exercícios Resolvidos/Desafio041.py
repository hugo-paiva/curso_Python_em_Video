print('\033[35m-==\033[m'*20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
idade = int(input('Qual é a sua idade? '))
if idade <= 9:
    categoria = 'Mirim'
elif idade <=14:
    categoria = 'Infantil'
elif idade <=19:
    categoria = 'Junior'
elif idade<=20:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print('Você tem {} anos e sua categoria é {}.'.format(idade, categoria))