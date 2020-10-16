from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in tupla:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')



'''from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for c in range(0, 5):
    if c == 0:
        maior = tupla[c]
        menor = tupla[c]
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]
print(f'Os valores sorteados foram {tupla}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''
