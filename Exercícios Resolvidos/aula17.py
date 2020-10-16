'''a = [2, 3, 4, 7]
b = a[:]
b[3] = 0
print(f'Lista A : {a}')
print(f'Lista B: {b}')'''






'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}!')
print('Cheguei ao final da lista.')'''






'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''


teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)