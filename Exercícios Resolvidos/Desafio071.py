print('-'*30)
print('{:^30}'.format('BANCO H'))
print('-'*30)
saque = int(input('Quanto você deseja sacar? R$'))
resto = saque
while resto > 0:
    if resto >= 50:
        nota = 50
    elif resto >= 20:
        nota = 20
    elif resto >= 10:
        nota = 10
    elif resto >= 1:
        nota = 1
    cedulas = resto // nota
    resto = resto % nota
    print(f'Total de {cedulas} cedulas de R${nota}')
print('='*30)
print('Volte sempre ao Banco H! Tenha um bom dia!')
