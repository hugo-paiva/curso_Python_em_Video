salario = float(input('Qual é o salário do funcionário?'))
# print(salario *1.1 if salario >1250 else salario * 1.15)
if salario < 1250:
    reajuste = salario * 1.1
else:
    reajuste = salario * 1.15
print('Seu salário de {}R${:.2f}{} após o reajuste passa a valer {}R${:.2f}{}'.format('\033[0;31m', salario, '\033[m',
                                                                                      '\033[4;36m', reajuste, '\033[m'))
