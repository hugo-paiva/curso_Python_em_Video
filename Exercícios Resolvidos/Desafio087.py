matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somcoluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        atual = matriz[l][c]
        if atual % 2 == 0:
            somapar += atual
        if c == 2:
            somcoluna += atual
        if l == 1:
            if c == 0 or atual > maior:
                maior = atual
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 30)
print(f'A soma de todos os valore pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somcoluna}')
print(f'O maior valor da segunda linha é {maior}')