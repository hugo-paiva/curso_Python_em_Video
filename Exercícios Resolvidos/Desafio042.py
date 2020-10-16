a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite o último número: '))
if a<b+c and b<a+c and c<a+b:
    print('Existe um triângulo com as medidas {}, {} e {}'.format(a, b, c))
    if a == b == c:
        tipo = 'Equilátero'
    elif a==b or a==c or b==c:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print('Com base no tamanho dos lados seu triângulo é {}.'.format(tipo))
else:
    print('Não é possível formar um triângulo.')


