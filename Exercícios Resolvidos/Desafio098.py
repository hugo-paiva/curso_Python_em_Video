from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    print('-=' * 25)
    print(f'Contagem de {i} até {f} de {-p if p < 0 else p} em {-p if p < 0 else p}')
    if i > f and p>0:
        p *= -1
        f -= 1
    if f > i:
        f += 1
    for c in range(i, f, p):
        print(f'{c} ', end='')
        sleep(0.2)
    print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' *25)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
