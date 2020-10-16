print('CALCULADORA DE IMC')
peso = float(input('Qual é o seu peso em Kg? '))
h = float(input('Qual é a sua altura em metros?'))
imc = peso/h**2
print('Seu Indice de Massa Corporal é {:.2f}'.format(imc))
if imc <18.5:
    print('\033[0;30;46mAbaixo do peso.\033[m')
elif 18.5<=imc<25:
    print('Peso ideal.')
elif 25<=imc<30:
    print('Sobrepeso.')
elif 30<=imc<40:
    print('Obesidade.')
else:
    print('\033[4;31mObesidade mórbida.\033[m')