from datetime import date
hoje = int(date.today().year)
cont = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = hoje - ano
    if idade >= 21:
        cont += 1
print('De 7 pessoas {} são maiores de idade e {} não são'.format(cont, 7-cont))
