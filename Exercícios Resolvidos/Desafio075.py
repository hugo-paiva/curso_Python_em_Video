tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 not in tupla:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.')
print(f'Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')