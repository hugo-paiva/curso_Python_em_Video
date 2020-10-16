#Faça um programa pra calcular o reajuste de salário em 15%
print('='*6 + ' REAJUSTE DE SALÁRIO ' + '='*6)
salario = float(input('Qual é o seu salário em reais?R$'))
reajuste = salario*1.15
print('O seu salário de R${:.2f}, com 15% de reajuste, é de R${:.2f}'.format(salario, reajuste))