'''n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número:'))

if n3 > n2:
    if n3 > n1:
        print("{} é o maior número.".format(n3))
    else:
        print('{} é o maior.'.format(n1))
else:
    if n2 > n1:
        print('{} é maior.'.format(n2))
    else:
        print('{} é o maior.'.format(n1))'''

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# Verificando quem é menor
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('\033[4;36mO menor valor é {}\033[m'.format(menor))
print('\033[4;35mO maior valor é {}\033[m'.format(maior))