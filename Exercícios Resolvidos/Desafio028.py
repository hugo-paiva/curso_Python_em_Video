num = int(input('Diga um número de 0 a 5: '))
from random import randint
n = randint(0, 5)
if n == num:
    print('Parabéns! Você acertou! Meu número é {}'.format(n))
else:
    print('Você errou! Era {}'.format(n))
