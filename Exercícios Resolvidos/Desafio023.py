num = int(input('Informe um número: '))
print('Analisando o número {}'.format(num))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('\033[31mUnidade: {}\033[m'.format(u))
print('\033[33mDezena: {}\033[m'.format(d))
print('\033[35mCentena: {}\033[m'.format(c))
print('\033[0;37mMilhar: {}\033[m'.format(m))

# Porém este método é falho e não recomendado por funcionar exclusivamente com 4 algarismos
'''num = str(input('Informe um número entre 0 e 9999: '))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))'''
