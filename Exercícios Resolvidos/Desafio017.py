from math import sqrt
import math
a = float(input('Qual é o valor do primeiro cateto?'))
b = float(input('Qual é o valor do segundo cateto?'))
h = sqrt(a ** 2 + b ** 2)

# Ou usa-se o termo mais simples
'''from math import hypot
h = hypot(a, b)'''

print('A hipotenusa de um triângulo de catetos de {} e {} equivale a {}'.format(a, b, h))
