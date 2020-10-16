'''print('======={}======='.format(' SEQUÊNCIA DE FIBONACCI '))
tottermos = int(input('Quantos termos você deseja mostra? '))
termo = 0
i = 0
j = 1
print('~'*30)
print('{}, {}, '.format(i, j), end='')
cont = 3
while cont <= tottermos:
    termo = i + j
    print('{}'.format(termo), end='')
    print(', ', end='' if cont < tottermos else ' => ')
    i = j
    j = termo
    cont += 1
print('Fim da Sequência')
print('~'*30)'''

print('='*20, ' SEQUÊNCIA DE FIBONACCI ', '='*20)
termos = int(input('Digite quantos termos você deseja mostrar: '))
t1 = 0
t2 = 1
t3 = 0
cont = 3
print('{} => {} => '.format(t1, t2), end='')
while cont <= termos:
    t3 = t2 + t1
    print('{}'.format(t3), end=' => ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')






