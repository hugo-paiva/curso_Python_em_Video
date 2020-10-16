print('-'*30)
print('{:^30}'.format('LOJA SUPER ECONOMIA'))
print('-'*30)
soma = contmil = ciclos = pechincha = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    soma += preço
    ciclos += 1
    if preço >= 1000:
        contmil += 1
    if ciclos == 1 or preço < pechincha:
        barato = nome
        pechincha = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {contmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${pechincha:.2f}')
