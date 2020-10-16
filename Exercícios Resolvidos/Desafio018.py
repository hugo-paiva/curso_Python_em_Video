from math import sin, cos, hypot
x = float(input('Digite um ângulo:'))
s = sin(x)
c = cos(x)
h = hypot(x)
print('Os valores trigonométricos do ângulo {} são {:.3f} para o seno, {:.3f} para o cosseno e {:.3f} para a hipotenusa.'.format(x, s, c, h))
