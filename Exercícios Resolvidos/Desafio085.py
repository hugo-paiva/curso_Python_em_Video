coleção = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        coleção[0].append(num)
    else:
        coleção[1].append(num)
print(f'Os valores pares digitados foram: {sorted(coleção[0])}')
print(f'Os valores impares digitados foram: {sorted(coleção[1])}')