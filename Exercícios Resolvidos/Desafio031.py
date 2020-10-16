d = int(input('Qual é a ditância da sua viagem em Km? '))
preço = d*0.5 if d<=200 else d*0.45
print('O preço da sua viagem é de R${:.2f}'.format(preço))


'''if d <=200:
    preço = d*0.5
    print('Sua passagem de {}Km custa {} reais. Boa viagem!'.format(d, preço))
else:
    preço = d*0.45
    print('Sua passagem de {}Km custa {} reais. Boa viagem!'.format(d, preço))'''

