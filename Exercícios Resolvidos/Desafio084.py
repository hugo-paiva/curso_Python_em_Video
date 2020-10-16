dados = []
pessoas = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')).title())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print('='*30)
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(p[0], end=' ')