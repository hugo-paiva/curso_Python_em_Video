'''def titulo(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)


# Programa Principal
titulo('oir')
titulo('python é foda')'''
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    soma = a + b
    print(f'A soma A + B = {soma}')


# Programa Principal
soma(b=4, a=5)'''
'''def contador(* num):
    print(f'Foi recebido {num} é o número de itens é {len(num)}')


# Programa Principal
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 3
        # lst[pos] = 2 * lst[pos]
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)