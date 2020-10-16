valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
par = []
imp = []
for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)
print('-='*40)
print(f'A lista completa é {valores}.')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {imp}')