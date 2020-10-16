lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
print('-='*50)
print(f'Você digitou os valores {lista}')
maior = max(lista)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
maiores = lista.count(maior)
posição = lista.index(maior)
print(posição, end=' ')
if maiores > 1:
    for c in range(0, maiores - 1):
        posição = lista.index(maior, posição + 1)
        print(posição, end=' ')
menor = min(lista)
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
menores = lista.count(menor)
pox = lista.index(menor)
print(pox, end=' ')
if menores > 1:
    for c in range(0, menores - 1):
        pox = lista.index(menor, pox + 1)
        print(pox, end=' ')