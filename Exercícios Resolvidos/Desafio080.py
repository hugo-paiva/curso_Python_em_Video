lista = []
for c in range(0, 5):
    new = int(input('Digite um valor: '))
    if c == 0:
        lista.append(new) or new > lista[-1]:
        print('Adicionado a última posição.')
    else:
        pos = 0
        while pos < len(lista):
            if new <= lista[pos]:
                lista.insert(pos, new)
                print(f'Adicionado a posição {pos} da lista.')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')

