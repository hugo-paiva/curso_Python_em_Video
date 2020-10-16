ficha = dict()
ficha['Nome'] = str(input('Nome: ')).title().strip()
ficha['Média'] = float(input(f'Média de {ficha["Nome"]}: '))
if ficha['Média'] >= 7:
    ficha['Situação'] = 'Aprovado'
elif 5 <= ficha['Média'] < 7:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Reprovado'
for k, v in ficha.items():
    print(f'{k} é igual a {v}')
