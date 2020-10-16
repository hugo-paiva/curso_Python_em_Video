print('-=='*20)
print('EMPRÉSTIMO BANCÁRIO')
print('-=='*20)
valor = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual é o seu salário atual? R$'))
anos = int(input('Em quantos anos pretende quitar o empréstimo? '))
prestação = valor/(anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} '.format(valor, anos, prestação))
if prestação <= salario*0.3:
    print('Seu empréstimo foi aceito.')
else:
    print('Seu empréstimo foi recusado.')