lista = []
coni = ' '
while True:
    new = int(input('Digite um valor: '))
    if new in lista:
        print('Valor duplicado. Não vou adicionar...')
    else:
        lista.append(new)
        print('Valor adicionado com sucesso...')
    while coni not in 'NS':
        coni = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    if coni == 'N':
        break
    else:
        coni = ' '
print('-='*40)
print(f'Você digitou os valores {sorted(lista)}')