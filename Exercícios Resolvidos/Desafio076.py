listagem = ('microondas', 450, 'televisão', 900, 'escova de dentes', 5, 'tenis', 120, 'sapato', 130)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
for c in range(0, len(listagem), 2):
    print('{:.<40}R${:>7.2f}'.format(listagem[c].capitalize(), listagem[c+1]))