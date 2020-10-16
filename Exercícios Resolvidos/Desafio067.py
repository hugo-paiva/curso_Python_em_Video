while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*40)
    for cont in range(0, 11):
        print(f'{n} x {cont:2} = {n*cont}')
    print('-'*40)
print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

