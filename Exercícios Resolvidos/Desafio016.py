'''import math
n = float(input('Digite um número: '))
n = math.trunc(n)
print('O seu número sem a casa decimal é {}'.format(n))'''

#Ou pelo seguinte caminho

'''from math import trunc
n = float(input('Digite o seu número: '))
n = trunc(n)
print('O seu número sem a casa decimal é {}'.format(n))'''

#Ou ainda sem importar nada. Basta converter para inteiro no final com a função int()

n = float(input('Digite um número decimal:'))
print('O seu número é {} e a porção inteira é {}'.format(n, int(n)))