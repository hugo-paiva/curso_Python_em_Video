'''num = int(input('Digite um número: '))
s = 0
d = 0
for c in range(0, num +1):
    s += 1
    print(s, end=' ')
    if num % s == 0:
        d = d + 1
if d > 2:
    print('não é primo')
else:
    print('é primo')'''

#
num = int(input('Digite um número: '))
s = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        s += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, s))
if s ==2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele NÃO É PRIMO')
